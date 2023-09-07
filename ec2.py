import boto3
import getCred

# Getting credentials from the .csv accesskey files
Credentials = getCred.get_credentials()

# Specifingy AWS credentials
aws_access_key_id = Credentials['AccessKey']
aws_secret_access_key = Credentials['SecertAccessKey']
region_name = 'us-east-1'

# Create an EC2 client
ec2 = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
instance_params = {
    'ImageId': 'ami-051f7e7f6c2f40dc1',
    'InstanceType': 't2.micro',  
    'KeyName': 'commvault-ec2-keypair', 
    'MinCount': 1,
    'MaxCount': 1,
}

# Launch the EC2 instance
response = ec2.run_instances(**instance_params)
print('Sucessfully Created EC2 INSTACNE')



