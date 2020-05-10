import sys
import boto3

INSTANCE_ID = sys.argv[1]

aws_ec2_client = boto3.client('ec2')

print(f"Delete instance: {INSTANCE_ID}")
response = aws_ec2_client.terminate_instances(InstanceIds=[INSTANCE_ID])
print(response)