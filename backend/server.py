from typing import Optional

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from starlette.requests import Request
from starlette.responses import HTMLResponse

from backend.barchart_interaction import fetch_options_overview

# from backend.barchart_interaction import handle_received_options_overview
from backend.constants import DB_URL
from backend.db_interaction import refresh_stocks_data_in_db
from backend.finviz_interaction import fetch_finviz_results

# from backend.finviz_interaction import handle_received_finviz_results
from backend.models import Stock as ModelStock
from backend.utils import handle_fetch


async def not_found(request, exc):
    """Returns header 404."""

    return HTMLResponse(
        content='<h1>404 - Page not found</h1>',
        status_code=exc.status_code,
    )


def extract_data_and_fill_db():
    """Asks for the new data from finviz and if succedes, refresh the db."""

    if finviz_results := handle_fetch(fetch_finviz_results):
        with db():
            refresh_stocks_data_in_db(db, finviz_results)


app = FastAPI(exception_handlers={404: not_found})
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)


@app.on_event('startup')
async def startup_event():
    """Launches the job that does the task. Starts with the app."""

    scheduler = AsyncIOScheduler()
    scheduler.start()
    scheduler.add_job(
        extract_data_and_fill_db,
        CronTrigger.from_crontab(
            '0 10-16 * * MON-FRI',
            timezone='America/New_York',
        ),
    )


@app.get('/')
def get_all_urls(request: Request) -> dict:
    """Shows all urls accessible in the app."""

    app_urls = {
        route.name: str(request.url).rstrip('/') + route.path
        for route in app.routes
        if hasattr(route, 'response_model') and route.path != '/'
    }

    return app_urls


@app.get('/stocks')
async def all_stocks() -> list:
    """Shows all stocks from db."""

    return db.session.query(ModelStock).all()


@app.get('/stocks/{ticker}')
async def stock_by_ticker(ticker: str) -> dict:
    """Shows some stock fundamentals for specific ticker.

    Arguments:
        ticker: ticker of stock to search info about
    """

    return db.session.query(ModelStock).filter_by(ticker=ticker).first()


@app.get('/options-overview/{ticker}')
async def options_overview_by_ticker(ticker: str) -> Optional[dict]:
    """Shows options overview for specific ticker.

    Arguments:
        ticker: ticker of stock to search info about
    """

    return handle_fetch(fetch_options_overview, ticker)
