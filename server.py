from utils import transform_json_from_list_to_dict_form
from fastapi import FastAPI

from finviz import fetch_finviz_results


app = FastAPI()


@app.get('/')
def home():
    finviz_results_in_list_format = fetch_finviz_results()
    return transform_json_from_list_to_dict_form(finviz_results_in_list_format)
