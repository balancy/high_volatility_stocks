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
        'cap_midover,fa_fpe_u50,sh_avgvol_o1000,sh_curvol_o500,sh_opt_option,'
        'ta_beta_o1,ta_perf_1wdown,ta_sma200_pa,ta_volatility_wo3'
    ),
    'c': '1,2,3,4,5,6,7,8,9,10,11,14,32,33,34,35,36,38,39,40,41,63',
}
