# Enode Python SDK (WIP)

I noticed that [Enode](https://enode.com/) does not have an official Python SDK—or any official SDK—so I'm creating one.

Very much a work in progress, but progress is being made.

## Features

- Lazy-init, lazy-fetch: API requests are not sent until data is accessed
- Automatic pagination: no need to manually handle cursors
- Automatic OAuth2 token request/refresh
- Automatic closing/releasing of resources
- Can be used as a context manager for faster releasing of resources