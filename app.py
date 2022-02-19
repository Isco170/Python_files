import aws_s3
from access import bucket

inicio = True
while inicio:
    aws_s3.upload_file(bucket)
    aws_s3.list_files(bucket)