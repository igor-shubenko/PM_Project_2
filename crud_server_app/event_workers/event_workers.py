import json
import os

import boto3

BUCKET_NAME = os.environ.get("BUCKET_NAME")
FILE_NAME = os.environ.get("FILE_NAME")
s3 = boto3.client('s3')


async def init_table_users(user_data_worker):
    with open('postgres_workers/SQL_scripts/create_table_users.sql', 'r') as f:
        create_table_script = f.read()
    await user_data_worker.execute_query(create_table_script)


async def download_file_from_s3():
    try:
        s3.download_file(BUCKET_NAME, FILE_NAME, FILE_NAME)
        print("Downloaded from S3")
    except Exception as e:
        print("Exception during download from S3: ", e)


async def write_to_postgres(user_data_worker):
    data_in_db = await user_data_worker.read_record('all')
    if not data_in_db:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                record = json.loads(line)
                record.pop('id')
                await user_data_worker.create_record(record)


async def write_to_file(user_data_worker):
    data = await user_data_worker.read_record('all')
    print("Data type is", type(data))
    try:
        with open(FILE_NAME, "w") as f:
            for record in data:
                f.write(json.dumps(record) + '\n')
            print("Wrote to file")
    except Exception as e:
        print("Exception during write to file: ", e)


async def upload_file_to_s3():
    try:
        with open(FILE_NAME, "rb") as f:
            s3.upload_fileobj(f, BUCKET_NAME, FILE_NAME)
            print("Uploaded to S3")
    except Exception as e:
        print("Exception during uploading to S3: ", e)
