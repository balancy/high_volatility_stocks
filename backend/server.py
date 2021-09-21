from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from starlette.responses import HTMLResponse

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


@app.get('/', response_class=HTMLResponse)
def get_all_urls():
    """Shows all urls accessible in the app."""

    url_list_in_html_format = [
        f'<li><a href="{route.path}">{route.name}</a></li>'
        for route in app.routes
    ]

    html_content = (
        '<html><head><title>App urls</title></head><body><ul>'
        f'{"".join(url_list_in_html_format)}'
        '</ul></body></html>'
    )

    return html_content


@app.get('/stocks', response_model=list)
def all_stocks():
    """Shows all stocks from db."""

    return db.session.query(ModelStock).all()
