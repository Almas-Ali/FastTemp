"""
Exceptions for fasttemp.
"""

__all__ = [
    'NotClosedException',
    'UndefinedVariableException',
]


class NotClosedException(Exception):
    """Raised when a block is not closed."""

    def __init__(self, message: str = 'Block not closed.') -> None:
        self.message = message
        super().__init__(self.message)


class UndefinedVariableException(Exception):
    """Raised when a variable is not defined."""

    def __init__(self, message: str = 'Variable not defined.') -> None:
        self.message = message
        super().__init__(self.message)
