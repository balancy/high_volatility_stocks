from typing import Optional, Union

from requests.exceptions import HTTPError, RequestException
from starlette.responses import HTMLResponse

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

    if value == '-':
        return None

    if value[-1] == '%':
        value = value[:-1]

    if 'on' in value or not value[-1].isdigit():
        return value

    if ',' in value:
        return int(value.replace(',', ''))

    return float(value)


def get_modified_key(key: str) -> str:
    """Modifies the key for db field.
    DB fields couldn't contain spaces and the symbol /. Function modifies keys
    received from parsing to DB fields format.

    Arguments:
        key: key_to_modify

    Returns:
        modified_key
    """

    return key.lower().replace(' ', '__').replace('/', '_')


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


def get_tickers_to_delete_update_add(
    tickers_in_db: list,
    tickers_in_new_data: list,
) -> list:
    """Gets tickers of stocks to delete from, to update to, to add to the
    database.

    Arguments:
        tickers_in_db: Tickers that are in the database
        tickers_in_new_data: New tickers needed to be in the database

    Returns:
        tickers to delete, to update and to add to the database
    """

    tickers_to_delete = [
        ticker for ticker in tickers_in_db if ticker not in tickers_in_new_data
    ]

    tickers_to_add = [
        ticker for ticker in tickers_in_new_data if ticker not in tickers_in_db
    ]

    tickers_to_update = [
        ticker for ticker in tickers_in_db if ticker in tickers_in_new_data
    ]

    return tickers_to_delete, tickers_to_update, tickers_to_add


def get_modified_data(data: list) -> list:
    """Modify data to be in corresponding to db records form.
    It modifies keys to be correct field names of db model and fixes values.

    Arguments:
        data: data containing values and keys to fix

    Returns:
        modified data
    """

    modified_data = list()

    for record in data:
        modified_data.append(
            {
                get_modified_key(key): fix_value(value)
                for key, value in record.items()
            }
        )

    return modified_data


async def not_found(request, exc):
    """Returns header 404."""

    return HTMLResponse(
        content='<h1>404 - Page not found</h1>',
        status_code=exc.status_code,
    )
