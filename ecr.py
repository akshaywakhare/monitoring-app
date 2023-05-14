import boto3

# creating ecr repository using boto3 client provided by aws
# this can also be manually done from aws console

ecr_client=boto3.client('ecr')

repository_name= "cloud_native_repo"
response = ecr_client.create_repository( 
    repositoryName=repository_name,
    imageScanningConfiguration={
        'scanOnPush': True
    },
    encryptionConfiguration={
        'encryptionType': 'AES256' 
    }
)

repository_uri=response['repository']['repositoryUri']

print(repository_uri)