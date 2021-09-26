from typing import Union

from requests.exceptions import HTTPError, RequestException
from starlette.responses import HTMLResponse

from app.logger.root import logger


def handle_fetch(fetch_function, ticker=None) -> Union[list, dict, None]:
    """Handles fetching with fetching function.
    If error occures during fetching or empty result returned, returns None and
    writes corresponding message to the logger.

    Arguments:
        fetch_function: function used to fetch data
        ticker: ticker if provided

    Returns:
        None or results if fetching succeded
    """

    try:
        results = fetch_function(ticker) if ticker else fetch_function()
    except (
        ConnectionError,
        HTTPError,
        RequestException,
        TimeoutError,
        Exception,
    ) as e:
        logger.error(
            f'Exception "{e}" occured during executing "{fetch_function}"'
        )
        return None

    if not results:
        logger.info(f'No results found during executing "{fetch_function}"')
        return None

    return results


async def not_found(request, exc):
    """Returns header 404."""

    return HTMLResponse(
        content='<h1>404 - Page not found</h1>',
        status_code=exc.status_code,
    )
