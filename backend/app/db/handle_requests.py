from fastapi_sqlalchemy import db as database
from fastapi_sqlalchemy.middleware import DBSessionMeta

from app.db.crud_operations import (
    add_records_to_db,
    delete_records_from_db,
    update_records_in_db,
)
from app.db.models import Stock
from app.sites_interaction.finviz import fetch_finviz_results
from app.utils.handle_errors import handle_fetch
from app.utils.handle_lists import get_tickers_to_delete_update_add
from app.utils.modify_data import get_modified_data


def refresh_db_with_stocks_data_from_finviz(
    db: DBSessionMeta, data: list
) -> None:
    """Delete the old ones records from the database, update the existing ones
    and add the new ones.

    Arguments:
        db: database to communicate with
        data: new data to analyse
    """

    (
        tickers_to_delete,
        tickers_to_update,
        tickers_to_add,
    ) = get_tickers_to_delete_update_add(
        [record.ticker for record in db.session.query(Stock).all()],
        [record['Ticker'] for record in data],
    )

    data = get_modified_data(data)

    delete_records_from_db(db, tickers_to_delete)
    update_records_in_db(db, tickers_to_update, data)
    add_records_to_db(db, tickers_to_add, data)


def extract_data_from_finviz_and_handle_db_operations():
    """Asks for the new data from finviz and if succedes, refreshes the db."""

    if finviz_results := handle_fetch(fetch_finviz_results):
        with database():
            refresh_db_with_stocks_data_from_finviz(database, finviz_results)
