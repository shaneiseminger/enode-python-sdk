from typing import Generic, TypeVar

from collections.abc import Callable

T = TypeVar('T')

class PageResponse(Generic[T]):

    def __init__(
            self,
            data: list[dict[str, object]],
            before: str | None,
            after: str | None,
            factory: Callable[[dict[str, object]], T],
    ):
        self._data: list[dict[str, object]] = data
        self._data_iter: iter = iter(self._data)
        self._before: str | None = before
        self._after: str | None = after
        self._factory: Callable[[dict[str, object]], T] = factory

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        return self.next()

    def next(self) -> T:
        return self._factory(next(self._data_iter))

    def __len__(self):
        return len(self.data)

    @property
    def data(self):
        return self._data

    @property
    def before(self):
        return self._before

    @property
    def after(self):
        return  self._after