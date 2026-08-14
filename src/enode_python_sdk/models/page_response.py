from typing import Generic, TypeVar

from collections.abc import Callable

T = TypeVar('T')

class PageResponse(Generic[T]):
    """Model a page from Enode as an iterable of objects.

    - Hydrates results using provided factory lambda
    - Makes hydrated results iterable
    - Exposes paginatino cursors"""

    def __init__(
            self,
            data: list[dict[str, object]],
            before: str | None,
            after: str | None,
            factory: Callable[[dict[str, object]], T],
    ):
        """Initialize PageResponse."""
        self._data: list[dict[str, object]] = data
        self._data_iter: iter = iter(self._data)
        self._before: str | None = before
        self._after: str | None = after
        self._factory: Callable[[dict[str, object]], T] = factory

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        """Support iterating."""
        return self.next()

    def next(self) -> T:
        """Support iterating.

        Hydrate results using the provided factory.
        """
        return self._factory(next(self._data_iter))

    def __len__(self):
        """Support len(PageResponse)."""
        return len(self.data)

    @property
    def data(self):
        """Expose a read-only 'data' property."""
        return self._data

    @property
    def before(self):
        """Expose a read-only 'before' property"""
        return self._before

    @property
    def after(self):
        """Expose a read-only 'after' property"""
        return  self._after