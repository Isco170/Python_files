from access import access_key, secret_access_key
import boto3
import os

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)