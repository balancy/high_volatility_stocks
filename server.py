from fastapi import FastAPI

from backend.finviz import (
    form_correct_response_for_api_demanding_finviz_results,
)

app = FastAPI()


@app.get('/')
def home():
    return form_correct_response_for_api_demanding_finviz_results()
