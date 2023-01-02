import json
import os

import boto3

from postgres_workers.users_worker import UserDataWorker

BUCKET_NAME = os.environ.get("BUCKET_NAME")
FILE_NAME = os.environ.get("FILE_NAME")
s3 = boto3.client('s3')


async def download_file_from_s3():
    try:
        s3.download_file(BUCKET_NAME, FILE_NAME, FILE_NAME)
        print("Downloaded from S3")
    except Exception as e:
        print("Exception during download from S3: ", e)


async def write_to_postgres(pool):
    postgres_writer = UserDataWorker(pool=pool)
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            record = json.loads(line)
            await postgres_writer.create_record(record)


async def write_to_file(pool):
    data = await UserDataWorker(pool=pool).read_record('all')
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
