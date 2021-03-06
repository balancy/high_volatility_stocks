from typing import Optional

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from app.sites_interaction.barchart import fetch_options_overview
from app.constants.db import DB_URL
from app.db.handle_requests import (
    extract_data_from_finviz_and_handle_db_operations,
)
from app.db.models import Stock
from app.utils.handle_errors import handle_fetch, not_found


app = FastAPI(
    exception_handlers={404: not_found},
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(DBSessionMiddleware, db_url=DB_URL),
    ]
)
# app.add_middleware(
#     Middleware(
#         CORSMiddleware,
#         allow_origins=[CORS_ORIGINS],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
# )
# app.add_middleware(DBSessionMiddleware, db_url=DB_URL)


@app.on_event('startup')
async def startup_event():
    """Launches the job that does the task. Starts with the app."""

    scheduler = AsyncIOScheduler()
    scheduler.start()
    scheduler.add_job(
        extract_data_from_finviz_and_handle_db_operations,
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


@app.get('/stocks/refresh')
async def refresh_stocks():
    """Refreshes manually stocks data in the databasse."""

    extract_data_from_finviz_and_handle_db_operations()

    return {'result': 'data is refreshed'}


@app.get('/stocks')
async def all_stocks() -> list:
    """Shows all stocks from db."""

    return db.session.query(Stock).all()


@app.get('/stocks/{ticker}')
async def stock_by_ticker(ticker: str) -> dict:
    """Shows some stock fundamentals for specific ticker.

    Arguments:
        ticker: ticker of stock to search info about
    """

    return db.session.query(Stock).filter_by(ticker=ticker).first()


@app.get('/options-overview/{ticker}')
async def options_overview_by_ticker(ticker: str) -> Optional[dict]:
    """Shows options overview for specific ticker.

    Arguments:
        ticker: ticker of stock to search info about
    """

    return handle_fetch(fetch_options_overview, ticker)
