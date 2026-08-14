from typing import Generic, Callable, Iterator, TypeVar

from enode_python_sdk.models.page_response import PageResponse

T = TypeVar('T')

class ResultCollection(Generic[T]):
    """Model a collection of results from Enode as an iterable of objects that will lazy-fetch pages

    - Full abstraction of pagination into a seamless iterable representing all results.
    - Uses a callable (lambda) that returns a PageResponse to fetch pages.
    """

    def __init__(self, fetch_page: Callable[[str | None], PageResponse[T]], ):
        # Store page loading lambda.
        self._fetch_page = fetch_page
        # Init _page_response, which will be loaded when ResultCollection is iterated.
        self._page_response: PageResponse[T] | None = None

    def __iter__(self) -> Iterator[T]:
        """Make this class an iterable."""
        return self

    def __next__(self):
        """Support iterating."""
        return self.next()

    def next(self):
        """Get next item in result collection, fetching next page if necessary."""
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
