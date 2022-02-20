import aws_s3
from access import bucket

inicio = True
while inicio:
    print("============== Fazendo upload de faturas ===================\n")
    aws_s3.upload_file(bucket)
    print("============= Enviando faturas por whatsapp ==================")
    aws_s3.list_files(bucket)