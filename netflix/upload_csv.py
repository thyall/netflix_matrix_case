import boto3

'''
  Creator: Thyall D'greville
  Data: Abril 2023
'''
# instanciando o client
s3 = boto3.client('s3')

# passando o nome do bucket
S3_BUCKET_NAME = 'caseconfitech'

# realizando upload
with open('netflix\output.csv', 'rb', ) as f:
  s3.upload_fileobj(f, S3_BUCKET_NAME, S3_BUCKET_NAME)