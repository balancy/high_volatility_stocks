from fastapi_sqlalchemy import db as database
from fastapi_sqlalchemy.middleware import DBSessionMeta

from backend.finviz_interaction import fetch_finviz_results
from backend.models import Stock
from backend.root_logger import logger
from backend.utils import (
    get_modified_data,
    get_tickers_to_delete_update_add,
    handle_fetch,
)


def delete_records_from_db(db: DBSessionMeta, tickers_to_delete: list) -> None:
    """Delete records containing specific tickers from the database.

    Arguments:
        db: database to delete records from
        tickers_to_delete: tickers of records to delete from the db
    """

    db.session.query(Stock).filter(
        Stock.ticker.in_(tickers_to_delete)
    ).delete()

    db.session.commit()

    if tickers_to_delete:
        logger.info(
            f'Tickers {", ".join(tickers_to_delete)} deleted from the '
            'Stocks table'
        )


def update_records_in_db(
    db: DBSessionMeta, tickers_to_update: list, data: list
) -> None:
    """Update records containing specific tickers in the database.

    Arguments:
        db: database to update records in
        tickers_to_update: tickers of records to update in the db
        data: data containing values to update
    """

    for record in [r for r in data if r['ticker'] in tickers_to_update]:
        db.session.query(Stock).filter(
            Stock.ticker == record['ticker']
        ).update(record)

    db.session.commit()

    logger.info(
        f'Tickers {", ".join(tickers_to_update)} updated in the Stocks table'
    )


def add_records_to_db(
    db: DBSessionMeta, tickers_to_add: list, data: list
) -> None:
    """Add new records containing specific tickers to the database.

    Arguments:
        db: database to add records to
        tickers_to_add: tickers of records to add to the db
        data: data containing values to add
    """

    for record in [r for r in data if r['ticker'] in tickers_to_add]:
        stock = Stock(**record)
        db.session.add(stock)

    db.session.commit()

    if tickers_to_add:
        logger.info(
            f'Tickers {", ".join(tickers_to_add)} added to the Stocks table'
        )


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


def extract_data_from_finviz_and_handles_db_operations():
    """Asks for the new data from finviz and if succedes, refreshes the db."""

    if finviz_results := handle_fetch(fetch_finviz_results):
        with database():
            refresh_db_with_stocks_data_from_finviz(database, finviz_results)
