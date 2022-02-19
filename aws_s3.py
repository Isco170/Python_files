from multiprocessing.connection import Client
from access import access_key, secret_access_key
import boto3
import os
from botocore.exceptions import NoCredentialsError
from botocore.client import Config
import ficheiros
url = './files/'

session = boto3.Session(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key   
)

s3 = session.resource('s3')


def gerarLink(buck, fich):
    try:
        link = boto3.client(
            's3',
            region_name='us-east-2',
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_access_key,
            config=Config(signature_version='s3v4')
            
            ).generate_presigned_url(
        ClientMethod='get_object', 
        Params={'Bucket': buck, 'Key': fich},
        ExpiresIn=3600)
        return link
    except:
        return False

def upload_file(bucket):
    ficheiros = os.listdir(url)
    if ficheiros:
        for ficheiro in ficheiros:
            try:
                object = s3.Object(bucket, ficheiro)
                result = object.put(Body = ficheiro)
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
        link = gerarLink(bucket, bu.key)
        if link:
            ficheiros.acao(link, bu.key)

# upload_file('franciscotest')
list_files('franciscotest')