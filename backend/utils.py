from typing import Optional, Union

from requests.exceptions import HTTPError, RequestException

from backend.root_logger import logger


def fix_value(value: str) -> Optional[float]:
    """Fixes value.
    If value represents -, returns None. If '%' or ',' in value, deletes it.
    If value contains on (like % on date), returns it as it is.

    Arguments:
        value: value to fix

    Returns:
        fixed value
    """

    value = value.strip()

    if 'on' in value:
        return value

    if value == '-':
        return None

    if ',' in value:
        return int(value.replace(',', ''))

    value = value.replace('%', '')

    return float(value)


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
