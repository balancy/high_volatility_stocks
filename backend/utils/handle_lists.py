def get_tickers_to_delete_update_add(
    tickers_in_db: list,
    tickers_in_new_data: list,
) -> list:
    """Gets tickers of stocks to delete from, to update to, to add to the
    database.

    Arguments:
        tickers_in_db: Tickers that are in the database
        tickers_in_new_data: New tickers needed to be in the database

    Returns:
        tickers to delete, to update and to add to the database
    """

    tickers_to_delete = [
        ticker for ticker in tickers_in_db if ticker not in tickers_in_new_data
    ]

    tickers_to_add = [
        ticker for ticker in tickers_in_new_data if ticker not in tickers_in_db
    ]

    tickers_to_update = [
        ticker for ticker in tickers_in_db if ticker in tickers_in_new_data
    ]

    return tickers_to_delete, tickers_to_update, tickers_to_add
