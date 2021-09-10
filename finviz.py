import json

import pandas as pd
import requests

from constants import (
    BROWSER_HEADERS,
    FINVIZ_PAGENUMBERS,
    FINVIZ_SCREENER_URL,
    FINVIZ_SEARCH_PARAMETERS,
)


def fetch_part_of_finviz_results(pagenumber: int) -> pd.DataFrame:
    """Fetches one part from finviz screener results.

    Finviz screener results are represented in several pages: overview,
    valuation, financial, performance. This function fetches only one page
    defined by pagenumber.

    Arguments:
        pagenumber: pagenumber to fetch one page from results

    Returns:
        data from one results page
    """

    params = {
        'v': pagenumber,
        'f': FINVIZ_SEARCH_PARAMETERS,
    }

    response = requests.get(
        url=FINVIZ_SCREENER_URL,
        headers=BROWSER_HEADERS,
        params=params,
    )
    response.raise_for_status()

    table = pd.read_html(response.content)[-2]
    table.columns = table.iloc[0]

    return table[1:]


def fetch_finviz_results() -> list:
    """Fetches results from finviz screener.

    Finviz screener results are represented in several pages: overview,
    valuation, financial, performance. This function fetches all these pages
    concatenated.

    Returns:
        results
    """

    finviz_results_df = fetch_part_of_finviz_results(FINVIZ_PAGENUMBERS[0])

    for pagenumber in FINVIZ_PAGENUMBERS[1:]:
        new_finviz_results = fetch_part_of_finviz_results(pagenumber)
        different_columns = new_finviz_results.columns.difference(
            finviz_results_df.columns
        )

        finviz_results_df = pd.merge(
            finviz_results_df,
            new_finviz_results[different_columns],
            left_index=True,
            right_index=True,
            how='inner',
        )

    finviz_results_df.drop('No.', axis=1, inplace=True)

    finviz_results_json = finviz_results_df.to_json(orient='records')
    finviz_results_parsed = json.loads(finviz_results_json)

    return finviz_results_parsed


if __name__ == '__main__':
    print(json.dumps(fetch_finviz_results(), indent=4))
