import os

from dotenv import load_dotenv


load_dotenv()
DB_URL = (
    f'postgresql+psycopg2://{os.getenv("POSTGRES_USER")}:'
    f'{os.getenv("POSTGRES_PASSWORD")}@db:{os.getenv("POSTGRES_PORT")}/'
    f'{os.getenv("POSTGRES_DB")}'
)
