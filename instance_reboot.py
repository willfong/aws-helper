import sys
import boto3

INSTANCE_ID = sys.argv[1]

aws_ec2_client = boto3.client('ec2')

print(f"Reboot instance: {INSTANCE_ID}")
response = aws_ec2_client.reboot_instances(InstanceIds=[INSTANCE_ID])
print(response)
