import os

from dotenv import load_dotenv


BARCHART_URL = 'https://www.barchart.com/stocks/quotes/'

BROWSER_HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebK'
        'it/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    )
}

FINVIZ_SCREENER_URL = 'https://finviz.com/screener.ashx'

FINVIZ_PARAMETERS = {
    'v': 152,
    'f': (
        'cap_midover,ipodate_more1,sh_avgvol_o500,sh_opt_option,'
        'ta_volatility_wo8'
    ),
    'c': '1,2,3,4,5,6,7,8,9,10,11,14,32,33,34,35,36,38,39,40,41,62,63',
}

load_dotenv()
DB_URL = (
    f'postgresql+psycopg2://{os.getenv("POSTGRES_USER")}:'
    f'{os.getenv("POSTGRES_PASSWORD")}@db:{os.getenv("POSTGRES_PORT")}/'
    f'{os.getenv("POSTGRES_DB")}'
)
