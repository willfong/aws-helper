import sys
import boto3
import base64


REPO_ID = sys.argv[1]
aws_ecr_client = boto3.client('ecr')

response = aws_ecr_client.describe_images(repositoryName=REPO_ID)

print(f"Repository Images: {REPO_ID}")

images = []

for image in response["imageDetails"]:
	print("x")
	images.append(f"[{image['imagePushedAt']}] {image['imageTags']}")

images.sort()

for image in images:
	print(image)