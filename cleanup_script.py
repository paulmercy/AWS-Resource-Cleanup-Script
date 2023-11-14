import boto3

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-2'  # replace with your preferred region
)

# Initialize the EC2 resource
ec2 = session.resource('ec2')

# Delete all EC2 instances
for instance in ec2.instances.all():
    instance.terminate()

# Initialize the S3 resource
s3 = session.resource('s3')

# Delete all S3 buckets
for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()

# Initialize the IAM resource
iam = session.resource('iam')

# Delete all IAM users
for user in iam.users.all():
    for access_key in user.access_keys.all():
        access_key.delete()
    for policy in user.policies.all():
        policy.delete()
    user.delete()

# Initialize the RDS resource
rds = session.client('rds')

# Delete all RDS instances
for db_instance in rds.describe_db_instances()['DBInstances']:
    rds.delete_db_instance(
        DBInstanceIdentifier=db_instance['DBInstanceIdentifier'],
        SkipFinalSnapshot=True
    )
