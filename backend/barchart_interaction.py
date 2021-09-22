# from typing import Optional
from datetime import datetime

from bs4 import BeautifulSoup
import requests

from backend.constants import (
    BARCHART_URL,
    BROWSER_HEADERS,
)

# from backend.root_logger import logger
from backend.utils import fix_value


def get_days_number_till_next_earnings_date(html: str) -> int:
    """Extracts the next earnings date from html content and counts number of
    days till that date.

    Arguments:
        html: html content

    Returns:
        number of days till extracted date
    """

    next_date_string = html.find(
        'span',
        text='Next Earnings Date',
    ).next_sibling.next_sibling.text.strip()

    next_date = datetime.strptime(next_date_string, '%m/%d/%y')

    return (next_date - datetime.today()).days


def fetch_options_overview(ticker: str) -> dict:
    """Fetches options overview from barchart page for corresponding ticker.

    Arguments:
        ticker: ticker to search options overview for

    Returns:
        overview
    """

    response = requests.get(
        url=BARCHART_URL + ticker,
        headers=BROWSER_HEADERS,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'lxml')

    options_overview = {
        li.select_one('.left').text: fix_value(li.select_one('.right').text)
        for li in soup.select('.bc-cot-table-wrapper li')
    }

    options_overview[
        'Days Till Next Earnings Date'
    ] = get_days_number_till_next_earnings_date(soup)

    return options_overview


# def handle_received_options_overview(ticker: str) -> Optional[dict]:
#     """Handles options overview fetched from barchart.
#     If error occures during fetching, returns None and
#     writes corresponding message to the logger.

#     Returns:
#         None or results if fetching succeded
#     """

#     try:
#         options_overview = fetch_options_overview(ticker)
#     except (
#         ConnectionError,
#         requests.exceptions.HTTPError,
#         TimeoutError,
#         Exception,
#     ) as e:
#         logger.error(
#             f'Exception "{e}" occured during fetching data from barchart',
#         )
#         return None

#     return options_overview


if __name__ == '__main__':
    ticker = 'AMC'
    print(fetch_options_overview(ticker))
