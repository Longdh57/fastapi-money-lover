from datetime import timedelta

from minio import Minio
from minio.error import ResponseError

from app.core.config import settings

minioClient = Minio(
    settings.MINIO_URL,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False,
)


def minio_list_buckets():
    try:
        bucket_list = minioClient.list_buckets()
        for bucket in bucket_list:
            print(bucket.name, bucket.created_date)
    except ResponseError as err:
        print(err)


def minio_make_bucket(bucket_name: str):
    try:
        minioClient.make_bucket(bucket_name)
    except ResponseError as err:
        print(err)


def minio_fput_object(bucket_name: str, obj_name: str, path: str, content_type: str):
    try:
        found = minioClient.bucket_exists(bucket_name)
        if not found:
            raise Exception(f"Bucket with name '{bucket_name}' is not exits")
        minioClient.fput_object(
            bucket_name=bucket_name,
            object_name=obj_name,
            file_path=path,
            content_type=content_type
        )
    except ResponseError as err:
        print(err)


def minio_get_object_url(bucket_name: str, obj_name: str):
    try:
        url = minioClient.presigned_get_object(bucket_name, obj_name, expires=timedelta(hours=1))
        print(url)
    except ResponseError as err:
        print(err)
