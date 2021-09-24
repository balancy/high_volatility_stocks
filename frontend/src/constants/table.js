export const tableHeaders = [
    'Ticker', 'Sector', 'Country', 'MCapit', 'P/E', 'Fwd P/E',
    'P/B', 'P/S', 'PEG', 'ROA', 'Debt/Eq', 'Q Ratio', 'Profit M', 'Recom',
]

export const tableFields = [
    {
        'name': 'ticker',
    },
    {
        'name': 'sector',
    },
    {
        'name': 'country',
    },
    {
        'name': 'market__cap',
    },
    {
        'name': 'p_e',
        'min_value': 15,
        'max_value': 50,
        'direct_order': true,
    },
    {
        'name': 'fwd__p_e',
        'min_value': 15,
        'max_value': 50,
        'direct_order': true,
    },
    {
        'name': 'p_b',
        'min_value': 1,
        'max_value': 5,
        'direct_order': true,
    },
    {
        'name': 'p_s',
        'min_value': 1,
        'max_value': 10,
        'direct_order': true,
    },
    {
        'name': 'peg',
        'min_value': 1,
        'max_value': 2,
        'direct_order': true,
    },
    {
        'name': 'roa',
        'min_value': 0,
        'max_value': 15,
        'direct_order': false,
    },
    {
        'name': 'debt_eq',
        'min_value': 0.1,
        'max_value': 0.5,
        'direct_order': true,
    },
    {
        'name': 'quick__r',
        'min_value': 0.5,
        'max_value': 3,
        'direct_order': false,
    },
    {
        'name': 'profit__m',
        'min_value': 0,
        'max_value': 25,
        'direct_order': false,
    },
    {
        'name': 'recom',
        'min_value': 2,
        'max_value': 3.5,
        'direct_order': true,
    },
]
