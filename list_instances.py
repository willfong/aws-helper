import boto3

aws_ec2_client = boto3.client('ec2')

response = aws_ec2_client.describe_instances()

def _read_tag(tags, key):
    for tag in tags:
        if tag['Key'] == key:
            return tag['Value']

for instance in response['Reservations'][1]['Instances']:
    print(f"{instance['InstanceId']}\t{instance['InstanceType']}\t{_read_tag(instance['Tags'], 'Name')}\t{instance['PublicDnsName']}")

