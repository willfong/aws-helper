import boto3

aws_ec2_client = boto3.client('ec2')

response = aws_ec2_client.describe_instances()

def _read_tag(tags, key):
    for tag in tags:
        if tag['Key'] == key:
            return tag['Value']

for reservation in response['Reservations']: 
    for instance in reservation['Instances']:
        print(f"{instance['InstanceId']}\t{_read_tag(instance['Tags'], 'Name')}\t{instance['InstanceType']}\t{instance['State']['Name']}\t{instance['PublicDnsName']}")

