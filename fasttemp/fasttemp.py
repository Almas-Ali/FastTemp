from typing import Unpack, Any, Self, Dict, Union
import re
import html
import bs4

import minify_html

from .exceptions import NotClosedException, UndefinedVariableException

__all__ = [
    'FastTemp',
]


class ContextMixin:
    """Mixin for context."""

    def add_context(self, **context: Unpack[Dict[Any, Any]]) -> Self:
        """Adds context to the template."""

        self.context.update(context)
        return self

    def _load_context(self) -> Self:
        """Loads the context."""

        # safe html in context
        self.context = {
            k: html.escape(v) for k, v in self.context.items() if isinstance(v, str)
        }

        try:
            self.template = re.sub(
                r'{{\s*([^{}]+)\s*}}',
                lambda match: str(self.context.get(match.group(1), '')),
                self.template,
            )
        except KeyError as exc:
            raise UndefinedVariableException(f'Variable {exc} is not defined.')

        return self


class ResolverMixin:
    """Mixin for resolvers."""

    def _apply_resolvers(self):
        """All kinds of resolvers are registed here."""

        # resolves starts with _resolve_*
        # Registed resolvers:
        self._resolve_comment()
        self._resolve_variable()
        self._resolve_safe()
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

    def _resolve_safe(self) -> Self:
        """Resolves the safe in the template."""

        def resolve_match(match):
            """Resolves a single match."""
            try:
                return match.group(1).format(**self.context)
            except KeyError as exc:
                raise UndefinedVariableException(
                    f'Variable {exc} is not defined.')

        # @safe ... @endsafe
        self.template = re.sub(
            r'@safe([^@]*)@endsafe',
            resolve_match,
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

    def _resolve_unless(self) -> Self:
        """Resolves the unless in the template."""
        ...

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


class FastTemp(
    ContextMixin,
    ResolverMixin,
):
    """FastTemp is a simple, fast, and lightweight template engine for Python."""

    def __init__(
        self,
        *,
        template: str,
        context: Union[Dict[Any, Any], None] = None,
        minify: bool = False,
        pretty: bool = False,
    ) -> None:
        """
        FastTemp is a simple, fast, and lightweight template engine for Python.

        Args:
            template (str): The template string.
            context (Dict[Any, Any], optional): The context variables. Defaults to None.
            minify (bool, optional): Whether to minify the template. Defaults to False.
            pretty (bool, optional): Whether to prettify the template. Defaults to False.
        """

        self.template = template
        self.minify = minify
        self.pretty = pretty

        if context is not None:
            self.context = context
            self.add_context(**context)
        else:
            self.context = {}

        # Resolve all resolvers
        self._apply_resolvers()
        # Load all context variables
        self._load_context()

    @classmethod
    def from_file(
        cls,
        *,
        file: str,
        context: Union[Dict[Any, Any], None] = None,
        minify: bool = False,
        pretty: bool = False,
    ) -> Self:
        """Creates a template from a file."""

        with open(file, 'r') as f:
            return cls(
                template=f.read(),
                context=context,
                minify=minify,
                pretty=pretty,
            )

    def __str__(self) -> str:
        if self.minify:
            return minify_html.minify(
                self.template,
                minify_css=True,
                minify_js=True,
                remove_processing_instructions=True,
                keep_closing_tags=True,
                keep_html_and_head_opening_tags=True,
            )
        elif self.pretty:
            return bs4.BeautifulSoup(self.template, 'html.parser').prettify()
        else:
            return self.template

    def __repr__(self) -> str:
        return f'<FastTemp template={self.template}>'

    def __all__(self) -> list:
        """Returns all available methods and properties."""
        return [
            'add_context',
            '__str__',
            '__repr__',
            '__all__',
            '__len__',
        ]

    def __len__(self) -> int:
        return len(self.template)
