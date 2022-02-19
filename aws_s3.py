import logging
from access import access_key, secret_access_key
import boto3
import os
from botocore.exceptions import NoCredentialsError, ClientError
from botocore.client import Config
import ficheirosManip
url = './files/'

session = boto3.Session(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key   
)

s3 = session.resource('s3')

s3_client = boto3.client(
    's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key 
    )

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


def upload(file_name, bucket, object_name = None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print("AQUI")
        logging.error(e)
        return False
    return True  


def upload_file(bucket):
    ficheiros = os.listdir(url)
    if ficheiros:
        for ficheiro in ficheiros:
            resposta = upload(url+ficheiro, bucket, ficheiro)
            print(f"Resposta: {resposta}")
    else:
        print("Sem faturas por enviar")


def list_files(bucket):
    my_bucket = s3.Bucket(bucket)
    for bu in my_bucket.objects.all():
        link = gerarLink(bucket, bu.key)
        if link:
            print(f"Link: {link}\n")

            ficheirosManip.acao(link, bu.key)  

def getInfo():
    s3_cl = boto3.client('s3',
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_access_key
        )
    version_id:str = s3_cl.head_object(
        Bucket='franciscotest', Key = '258845451323 - fds.pdf'
    )
    print(version_id)


# upload_file('franciscotest')
# list_files('franciscotest')