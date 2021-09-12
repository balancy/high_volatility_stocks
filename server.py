from finviz import form_correct_response_for_api_demanding_finviz_results
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def home():
    return form_correct_response_for_api_demanding_finviz_results()
