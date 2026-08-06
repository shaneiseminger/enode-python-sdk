from typing import Generic, Callable, Iterator, TypeVar

from enode_python_sdk.models.page_response import PageResponse

T = TypeVar('T')

class ResultCollection(Generic[T]):

    def __init__(self, fetch_page: Callable[[str | None], PageResponse[T]], ):
        self._fetch_page = fetch_page
        self._page_response: PageResponse[T] | None = None

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self):
        return self.next()

    def next(self):
        while True:
            if self._page_response is None:
                self._page_response = self._fetch_page(None)
            try:
                return self._page_response.next()
            except StopIteration:
                if self._page_response.after is None:
                    raise
                self._page_response = self._fetch_page(
                    self._page_response.after
                )
