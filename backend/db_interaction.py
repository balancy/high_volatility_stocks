from fastapi_sqlalchemy.middleware import DBSessionMeta

from backend.models import Stock
from backend.root_logger import logger
from backend.utils import fix_value


# TODO: can be made with less deletions and insertions, but is it necessary?
def refresh_stocks_data_in_db(database: DBSessionMeta, data: list) -> None:
    """Delete the old ones records from db and add the new ones.

    Arguments:
        database: database to communicate with
        data: data to add to database
    """

    num_records_deleted = database.session.query(Stock).delete()
    logger.info(f'{num_records_deleted} deleted from the Stocks table')
    database.session.commit()

    for record in data:
        db_stock = Stock(
            ticker=record.get('Ticker'),
            company=record.get('Company'),
            sector=record.get('Sector'),
            industry=record.get('Industry'),
            country=record.get('Country'),
            market_cap=record.get('Market Cap'),
            pe=fix_value(record.get('P/E')),
            forward_pe=fix_value(record.get('Fwd P/E')),
            peg=fix_value(record.get('PEG')),
            ps=fix_value(record.get('P/S')),
            pb=fix_value(record.get('P/B')),
            div=fix_value(record.get('Dividend')),
            roa=fix_value(record.get('ROA')),
            roe=fix_value(record.get('ROE')),
            roi=fix_value(record.get('ROI')),
            curr_r=fix_value(record.get('Curr R')),
            quick_r=fix_value(record.get('Quick R')),
            debt_eq=fix_value(record.get('Debt/Eq')),
            gross_m=fix_value(record.get('Gross M')),
            oper_m=fix_value(record.get('Oper M')),
            profit_m=fix_value(record.get('Profit M')),
            volume=record.get('Avg Volume'),
        )
        database.session.add(db_stock)
        logger.info(f'{db_stock} added to Stocks table')

    database.session.commit()
