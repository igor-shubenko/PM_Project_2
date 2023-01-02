import json
import os

import boto3

from postgres_workers.users_worker import UserDataWorker

BUCKET_NAME = os.environ.get("BUCKET_NAME")
FILE_NAME = os.environ.get("FILE_NAME")
s3 = boto3.client('s3')


def download_file_from_s3():
    try:
        s3.download_file(BUCKET_NAME, FILE_NAME, FILE_NAME)
        print("Downloaded from S3")
    except Exception as e:
        print("Exception during download from S3: ", e)


def write_to_file(pool):
    data = UserDataWorker(pool=pool).read_record('all')
    print("Data type is", type(data))
    try:
        with open(FILE_NAME, "w") as f:
            for record in data:
                f.write(json.dumps(record) + '\n')
            print("Wrote to file")
    except Exception as e:
        print("Exception during write to file: ", e)


def upload_file_to_s3():
    try:
        with open(FILE_NAME, "rb") as f:
            s3.upload_fileobj(f, BUCKET_NAME, FILE_NAME)
            print("Uploaded to S3")
    except Exception as e:
        print("Exception during uploading to S3: ", e)




