from typing import Unpack, Any, Self, Dict, Union
import re

from .exceptions import NotClosedException, UndefinedVariableException

__all__ = [
    'FastTemp',
]


class FastTemp:
    """A simple template engine."""

    def __init__(
        self,
        template: str,
        context: Union[Dict[Any, Any], None] = None,
    ) -> None:
        self.template = template

        if context is not None:
            self.context = context
            self.add_context(**context)
        else:
            self.context = {}

        # Resolve all resolvers
        self._resolvers()
        # Load all context variables
        self._load_context()

    def add_context(self, **context: Unpack[Dict[Any, Any]]) -> Self:
        """Adds context to the template."""

        self.context.update(context)
        return self

    def _load_context(self) -> Self:
        """Loads the context."""

        try:
            self.template = self.template.format(**self.context)
        except KeyError as exc:
            raise UndefinedVariableException(f'Variable {exc} is not defined.')

        return self

    def _resolvers(self):
        """All kinds of resolvers are listed here."""

        self._resolve_comment()
        self._resolve_variable()
        self._resolve_conditional()
        self._resolve_python()

    def _resolve_variable(self) -> Self:
        """Resolves the variables in the template."""

        def resolve_set_variable(match):
            """Resolves a set variable match."""
            variable = match.group(1).strip()
            value = match.group(2).strip()

            self.context[variable] = eval(value)

            return ''

        # @set(my_var, 'Hello, World!')
        self.template = re.sub(
            r'@set\(([^,]+)(?:,\s*(.*?)|)\)',
            resolve_set_variable,
            self.template,
            flags=re.DOTALL,
        )

        return self

    def _resolve_comment(self) -> Self:
        """Resolves the comments in the template."""

        # @comment This is a comment @endcomment
        self.template = re.sub(
            r'@comment([^@]*)@endcomment',
            lambda m: '',
            self.template,
            flags=re.DOTALL,
        )

        return self

    def _resolve_conditional(self) -> 'FastTemp':
        """Resolves the conditional in the template."""

        def resolve_match(match):
            """Resolves a single match."""

            condition = match.group(1).strip()
            true_content = match.group(2).strip()

            if eval(condition, self.context):
                return true_content
            else:
                return ''

        def resolve_double_match(match):
            """Resolves a double match."""
            condition = match.group(1).strip()
            true_content = match.group(2).strip()
            remaining_content = match.group(3).strip()

            if eval(condition, self.context):
                return true_content
            else:
                return remaining_content

        def resolve_ladder_match(match):
            """Resolves a ladder match."""
            condition = match.group(1).strip()
            true_content = match.group(2).strip()
            remaining_content = match.group(3).strip()

            if eval(condition, self.context):
                return true_content
            else:
                return remaining_content

        while '@if' in self.template:
            if '@endif' not in self.template:
                raise SyntaxError('Invalid syntax: Missing @endif')

            # @if(condition) true @elif true @elif true @endif
            self.template = re.sub(
                r'@if\(([^)]*)\)([^@]*)@elif([^@]*)@endif',
                resolve_ladder_match,
                self.template,
                flags=re.DOTALL,
            )

            # @if(condition) true @else false @endif
            self.template = re.sub(
                r'@if\(([^)]*)\)([^@]*)@else([^@]*)@endif',
                resolve_double_match,
                self.template,
                flags=re.DOTALL,
            )

            # @if(condition) true @endif
            self.template = re.sub(
                r'@if\(([^)]*)\)([^@]*)@endif',
                resolve_match,
                self.template,
                flags=re.DOTALL,
            )

            # @if(condition) true @elif true @endif
            self.template = re.sub(
                r'@if\(([^)]*)\)([^@]*)(@elif\(([^)]*)\)([^@]*)|@else([^@]*))?@endif',
                lambda m: resolve_match(m)
                if eval(m.group(1).strip(), self.context)
                else m.group(5).strip()
                if m.group(5)
                else m.group(3).strip(),
                self.template,
                flags=re.DOTALL,
            )

        return self

    def _resolve_python(self) -> Self:
        """Resolves the python in the template."""

        if '@python' in self.template:
            if '@endpython' not in self.template:
                raise NotClosedException

            self.template = re.sub(
                r'@python([^@]*)@endpython',
                lambda m: exec(m.group(1)),
                self.template,
                flags=re.DOTALL,
            )

        return self

    def __str__(self) -> str:
        return self.template

    def __repr__(self) -> str:
        return f'<FastTemp template={self.template}>'

    def __len__(self) -> int:
        return len(self.template)
