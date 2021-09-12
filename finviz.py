import json
import sys

import pandas as pd
import requests
from requests.models import HTTPError
from requests.sessions import TooManyRedirects

from constants import (
    BROWSER_HEADERS,
    FINVIZ_SCREENER_URL,
    FINVIZ_PARAMETERS,
)
from utils import transform_json_from_list_to_dict_form


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

    table = pd.read_html(response.content)[-2]
    table.columns = table.iloc[0]

    table_in_json_format = table[1:].to_json(orient='records')

    return json.loads(table_in_json_format)


def form_correct_response_for_api_demanding_finviz_results() -> dict:
    """Formes the correct response to API endpoint.

    If an API endpoint demands for finviz results, it fetches the results.
    If fetching is successful, returns the results in the correct form. If not,
    returns predefined dictionary.

    Return:
        results
    """

    try:
        finviz_results = fetch_finviz_results()
    except (
        ConnectionError,
        HTTPError,
        TimeoutError,
        TooManyRedirects,
        Exception,
    ):
        ex_type, _, _ = sys.exc_info()
        return {
            'error': f'{ex_type.__name__} was occured during fetching data',
        }

    if not finviz_results:
        return {'results': 'no results found'}

    return transform_json_from_list_to_dict_form(finviz_results)


if __name__ == '__main__':
    print(form_correct_response_for_api_demanding_finviz_results(), indent=4)
