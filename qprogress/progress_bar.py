from typing import Callable, Any, Tuple

from .formatters import default_format_func


class ProgressBar:
    def __init__(self, iterable: Tuple[Any], format_func: Callable[[int, int], None] = default_format_func):
        if not isinstance(iterable, tuple):
            iterable = tuple(iterable)
        self.length = len(iterable)
        self.index = 0
        self.iterable = iterable
        self.format_func = format_func

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_item = self.iterable[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        self.format_func(self.index, self.length)
        return next_item
