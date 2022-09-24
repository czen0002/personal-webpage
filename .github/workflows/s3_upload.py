from botocore.exceptions import ClientError
import os
import sys
import boto3


def get_file_extension(file_name):
    _, file_extension = os.path.splitext(file_name)
    return file_extension


def get_content_type(file_name):
    file_extension = get_file_extension(file_name);
    if file_extension == '.json':
        return 'application/json'
    elif file_extension == '.js':
        return 'application/javascript'
    elif file_extension == '.html':
        return 'text/html'
    elif file_extension == '.ico':
        return 'image/x-icon'
    elif file_extension == '.txt':
        return 'text/plain'
    elif file_extension == '.css':
        return 'text/css'
    elif file_extension == '.map':
        return 'application/javascript'
    elif file_extension == '.jpg':
        return 'image/jpeg'
    else:
        return 'application/octet-stream'


def delete_files_in_s3_folder(s3_client, bucket, prefix):
    try:
        response = s3_client.list_objects_v2(
            Bucket=bucket,
            Prefix=prefix
        )
    except ClientError:
        print('ClientError raised when get objects in s3 bucket')
        raise

    if 'Contents' in response:
        for ob in response['Contents']:
            try:
                s3_client.delete_object(
                    Bucket=bucket,
                    Key=ob['Key']
                )
            except ClientError:
                print('ClientError raised when delete objects in s3 bucket')
                raise
    print('Deleted files in folder')


def s3_upload(s3_client, bucket, folder):
    for root, _, files in os.walk(folder):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            try:
                s3_client.put_object(
                    Bucket=bucket,
                    Body=open(full_path, 'rb'),
                    Key=full_path[len(folder) + 1:],
                    ContentType=get_content_type(full_path)
                )
            except ClientError:
                print('ClientError raised when put object in s3 bucket')
                raise
    print('Upload all files to s3 bucket')


if __name__ == '__main__':
    BUCKET = sys.argv[1]
    FOLDER = 'build'
    JS_PREFIX = 'static/js/'
    CSS_PREFIX = 'static/css/'
    MEDIA_PREFIX = 'static/media/'
    S3 = 's3'

    s3_client = boto3.client(S3)
    delete_files_in_s3_folder(s3_client, BUCKET, JS_PREFIX)
    delete_files_in_s3_folder(s3_client, BUCKET, CSS_PREFIX)
    delete_files_in_s3_folder(s3_client, BUCKET, MEDIA_PREFIX)
    s3_upload(s3_client, BUCKET, FOLDER)
