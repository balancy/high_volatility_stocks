TICKER_KEY = 'Ticker'


def transform_json_from_list_to_dict_form(json_list: list) -> dict:
    """Transforms json from list to dictionary form using Ticker value as key.

    Example:
    [
        {'Ticker': 'AAPL', 'Price': '249', ...},
        {'Ticker': 'MSFT', 'Price': '127', ...},
        ...
    ] will transform to
    {
        'AAPL': {'Price': '249', ...},
        'MSFT': {'Price': '127', ...},
        ...
    }

    Arguments:
        json_list: initial json in list form

    Return:
        transformed json in dictionary form
    """

    json_dict = dict()

    for record in json_list:
        ticker = record.get(TICKER_KEY)
        json_dict[ticker] = {
            key: value for key, value in record.items() if key != TICKER_KEY
        }

    return json_dict
