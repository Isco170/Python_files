from multiprocessing.connection import Client
from access import access_key, secret_access_key
import boto3
import os
from botocore.exceptions import NoCredentialsError
url = './files/'

session = boto3.Session(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key   
)

s3 = session.resource('s3')

def upload_file(bucket):
    ficheiros = os.listdir(url)
    if ficheiros:
        for ficheiro in ficheiros:
            try:
                object = s3.Object(bucket, ficheiro)
                result = object.put(Body = ficheiro)
                print("Upload successful")
                # try:
                link = s3.generate_presigned_url(
                    ClientMethod = 'put_object',
                    Params = {
                        'Bucket': bucket,
                        'Key': ficheiro
                    }
                )
                print(f"Link: {link}")
                # except:
                    # print('Sem link')
                # return True
            except FileNotFoundError:
                print("The file was not found")
                # return False
            except NoCredentialsError:
                print("Credentials not available")
                # return False

def list_files(bucket):
    my_bucket = s3.Bucket(bucket)
    for bu in my_bucket.objects.all():
        print(bu.key)

upload_file('franciscotest')
# list_files('franciscotest')
