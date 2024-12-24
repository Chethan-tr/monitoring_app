import boto3

aws_ecr_client = boto3.client('ecr')

repository_name = "monitoring_app_repo"
response = aws_ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']

print(repository_uri, repository_name)
