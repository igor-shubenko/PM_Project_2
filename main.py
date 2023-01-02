import logging

from fastapi import FastAPI
import uvicorn
import boto3

BUCKET_NAME = "pm-bucket-project"
file_from_s3 = "data.jsonl"
s3 = boto3.client('s3')

app = FastAPI()


@app.on_event("startup")
def startup_event():
    s3.download_file(BUCKET_NAME, file_from_s3, file_from_s3)


@app.get('/hello')
def hello():
    with open(file_from_s3, "a") as f:
        f.write("Happy New Year 2023!")
    return {"Message": "Hello students of PM group 1!"}


@app.on_event("shutdown")
def shutdown_event():
    with open(file_from_s3, "rb") as f:
        s3.upload_fileobj(f, BUCKET_NAME, file_from_s3)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=1)
