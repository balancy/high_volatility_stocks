import os

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from dotenv import load_dotenv

from .finviz import (
    form_correct_response_for_api_demanding_finviz_results,
)
from .models import Stock as ModelStock
from .schema import Stock as SchemaStock


load_dotenv()
app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.getenv('DB_URL'))


@app.get('/')
def home():
    return form_correct_response_for_api_demanding_finviz_results()


@app.post('/stock/', response_model=SchemaStock)
def write_stock_to_db(stock: SchemaStock):
    db_stock = ModelStock(ticker=stock.ticker)
    db.session.add(db_stock)
    db.session.commit()
    return db_stock
