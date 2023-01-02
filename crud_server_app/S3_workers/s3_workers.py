import boto3

BUCKET_NAME = "ispectre-test-bucket"
file_from_s3 = "data.jsonl"
s3 = boto3.client('s3')


def download_file_from_s3():
    try:
        s3.download_file(BUCKET_NAME, file_from_s3, file_from_s3)
    except Exception as e:
        print("Exception during download from S3: ", e)


def write_to_file():
    try:
        with open(file_from_s3, "a") as f:
            f.write("Happy New Year 2023!")
    except Exception as e:
        print("Exception during write to filw: ", e)



def upload_file_to_s3():
    try:
        with open(file_from_s3, "rb") as f:
            s3.upload_fileobj(f, BUCKET_NAME, file_from_s3)
    except Exception as e:
        print("Exception during uploading to S3: ", e)




