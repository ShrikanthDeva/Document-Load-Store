import boto3
import getCred
import os

# Getting credentials from the .csv accesskey files
Credentials = getCred.get_credentials()
source_folder = os.getcwd()+"/docs"

# Specifingy AWS credentials
aws_access_key_id = Credentials['AccessKey']
aws_secret_access_key = Credentials['SecertAccessKey']
region_name = 'us-east-1'
bucket_name = "commvault-user-bucket"

# intialising the s3 client
s3 = boto3.client('s3',region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

def upload_file_in_s3(file_name):

    try:
        file_path = f"{source_folder}/{file_name}"

        s3.upload_file(file_path, bucket_name, file_name)        
        print(f"File '{file_name}' uploaded to S3 as '{file_name}'")

    except Exception as e:
        print(f"Error uploading file to S3: {str(e)}")
    
def check_file_exists_in_s3(file_name):

    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=file_name)

        for obj in response.get('Contents', []):
            if obj['Key'] == file_name:
                return True
        return False
    
    except Exception as e:
        print(f"Error checking file existence in S3: {str(e)}")
        return False


def download_file_from_s3(file_name, local_file_path):
    try:
        s3.download_file(bucket_name, file_name, local_file_path)
        print(f"File '{file_name}' downloaded from S3 to '{local_file_path}'")
        return True

    except Exception as e:
        print(f"Error downloading file from S3: {str(e)}")
        return False