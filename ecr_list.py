import boto3
import base64

aws_ecr_client = boto3.client('ecr')

response = aws_ecr_client.describe_repositories()

for repo in response['repositories']:
    response = aws_ecr_client.get_authorization_token(registryIds=[repo['registryId']])
    print(f"{repo['repositoryName']}\t{repo['repositoryArn']}")
    #print(f"  {response['authorizationData'][0]['proxyEndpoint']}")
    #print(response['authorizationData'][0]['authorizationToken'])
