import boto3

aws_route53_client = boto3.client('route53')

response = aws_route53_client.list_hosted_zones()

for zone in response['HostedZones']:
    print(f"{zone['Id']}\t{zone['Name']}")
    record_sets = aws_route53_client.list_resource_record_sets(HostedZoneId=zone['Id'])
    for record in record_sets['ResourceRecordSets']:
        print(f"  {record['Name']} ({record['Type']})")

