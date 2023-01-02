import os

from fastapi import FastAPI
from psycopg_pool import AsyncConnectionPool

from postgres_workers.users_worker import UserDataWorker
from postgres_workers.events_worker import EventsDataWorker
from postgres_workers.bets_worker import BetsDataWorker
from S3_workers.s3_workers import download_file_from_s3, upload_file_to_s3, write_to_file, write_to_postgres

connection_string = os.environ.get("DATABASE_LINK")
pool = AsyncConnectionPool(connection_string, open=False)


def startup_event_handler(app: FastAPI):
    async def wrapper():
        app.user_data_worker = UserDataWorker(pool=pool)
        await pool.open(wait=True)
        await download_file_from_s3()
        await write_to_postgres(app.user_data_worker)
    return wrapper


def shutdown_event_handler(app: FastAPI):
    async def wrapper():
        await write_to_file(app.user_data_worker)
        await upload_file_to_s3()
        await pool.close()
    return wrapper
