import json
import sys
from typing import Optional

import pandas
import requests

from backend.constants import (
    BROWSER_HEADERS,
    FINVIZ_SCREENER_URL,
    FINVIZ_PARAMETERS,
)
from backend.root_logger import logger


def fetch_finviz_results() -> list:
    """Fetches the results from finviz screener.

    Finviz results accoring to search and display parameters.

    Returns:
        results
    """

    response = requests.get(
        url=FINVIZ_SCREENER_URL,
        headers=BROWSER_HEADERS,
        params=FINVIZ_PARAMETERS,
    )
    response.raise_for_status()

    table = pandas.read_html(response.text)[-2]
    table.columns = table.iloc[0]

    table_in_json_format = table[1:].to_json(orient='records')

    return json.loads(table_in_json_format)


def handle_received_finviz_results() -> Optional[list]:
    """Handles finviz results.
    If error occured during fetching or empty list returned, returns None and
    writes corresponding message to the logger.

    Returns:
        None or results if fetching succeded
    """

    try:
        finviz_results = fetch_finviz_results()
    except (
        ConnectionError,
        TimeoutError,
        Exception,
    ):
        ex_type, _, _ = sys.exc_info()
        logger.exception(
            {ex_type.__name__} + ' occured during fetching data from finviz'
        )
        return None

    if not finviz_results:
        logger.info('No results found during fetching data from finviz')
        return None

    return finviz_results


if __name__ == '__main__':
    print(
        json.dumps(
            fetch_finviz_results(),
            indent=4,
        )
    )
