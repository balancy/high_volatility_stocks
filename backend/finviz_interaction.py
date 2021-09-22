import json

import pandas
import requests

from backend.constants import (
    BROWSER_HEADERS,
    FINVIZ_SCREENER_URL,
    FINVIZ_PARAMETERS,
)


def fetch_finviz_results() -> list:
    """Fetches the results from finviz screener.

    Fetches results accoring to search and display parameters.

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


if __name__ == '__main__':
    print(
        json.dumps(
            fetch_finviz_results(),
            indent=4,
        )
    )
