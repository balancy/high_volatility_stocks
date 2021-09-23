BARCHART_URL = 'https://www.barchart.com/stocks/quotes/'

BROWSER_HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebK'
        'it/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    )
}

CORS_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://localhost:3000',
]

FINVIZ_SCREENER_URL = 'https://finviz.com/screener.ashx'

FINVIZ_PARAMETERS = {
    'v': 152,
    'f': 'cap_midover,fa_peg_u1,sh_avgvol_o1000,ta_volatility_wo4',
    'c': '1,2,3,4,5,6,7,8,9,10,11,14,32,33,34,35,36,38,39,40,41,62,63',
}
