from fastapi_sqlalchemy.middleware import DBSessionMeta

from backend.db.models import Stock
from backend.logger.root import logger


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

    if tickers_to_update:
        logger.info(
            f'Tickers {", ".join(tickers_to_update)} updated in the Stocks '
            'table'
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
