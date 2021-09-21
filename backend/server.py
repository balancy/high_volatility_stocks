from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db

from backend.constants import DB_URL
from backend.db_interaction import refresh_stocks_data_in_db
from backend.finviz_interaction import handle_received_finviz_results
from backend.models import Stock as ModelStock


app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)


def extract_data_and_fill_db():
    """Asks for the new data from finviz and if succedes, refresh the db."""

    if finviz_results := handle_received_finviz_results():
        with db():
            refresh_stocks_data_in_db(db, finviz_results)


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
def home():
    return db.session.query(ModelStock).all()
