# Load-Store-Application using boto3

+ This is a flask based application for load and storing the documents to the s3 bucket


## STEPS DONE:
+ created a AWS root user account
+ created IAM role for commvault-interview process with minimal roles  ( ec2& s3)
+ created Access key
+ created ec2-key pair
+ boto3 python program to launch an ec2 instance using the credentials
+ created a flask app:
  + 3 functionality -> search, download, upload
  + 3 templates for the same
+ uploaded the flask prgm to github
+ ssh into the ec2 instance and performed the basic scripts
+ fetched the flask prgm from github repo
+ runned the program on the ec2 instance
# working appln in my local machine
## Home page 
![Home-page](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/79d5e3df-0dec-4ab4-af2e-2873f705adf1)
## Upload page
![upload-1](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/11cf3f59-c90d-4cbc-be12-8c90d2efc847)
![upload-2](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/7df211b4-d6e1-4746-80a4-a5428bca1648)
![upload-3](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/06d08bfb-4c68-4590-afcf-7762b5e8ab06)
## Search page
![Search-1](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/eef527d2-606d-4ae1-a1bf-67810b7617aa)
#### FOUND CASE
![Search-2](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/c91c8d0b-01d6-493a-b475-ba2a33fc48d0)
![Search-3](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/832b3daf-b67b-4b62-adc6-52be89a932b4)
#### NOT FOUND CASE
![Search-4](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/23ae2000-7108-450b-b460-edc4e9b8d788)
![Search-5](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/67486d7f-e69d-40f7-9457-146a83a02c60)
## Download page
![Download-1](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/38ea2920-a90f-4f52-a4e9-204ee3355630)
#### FOUND CASE
![Download-2](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/f5c8a888-a388-4c0e-82be-74feeee860c6)
![Download-3](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/a2332c74-dad2-4b82-bb14-b20d0e031a59)
#### NOT FOUND CASE
![Download-4](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/4f2f6817-818c-45a4-a4f8-729b5d46ad4b)
![Download-5](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/8c32db1d-bc20-4d41-8db0-4cf4b596e96a)


## EC2 INSTANCE
![Ec2-on-aws](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/49628a01-ed33-4e79-a99b-109e6da9cb4c)

## S3 BUCKET
![S3-bucket](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/769f2595-4637-44c9-9d83-b067b4ad3961)

## IAM USER FOR seprate user not using root user for confidential purpose
![IAM-1](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/0ceda009-43e4-44ce-976a-5c97d6e6b604)

![IAM-2](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/bc0bad3a-137a-4a09-b03e-595f94b24a40)



## DEPLOYMENT
+ could locally run the application on the ec2 instance but not deploy it
![App-on-EC2](https://github.com/ShrikanthDeva/Document-Load-Store/assets/94846398/c0bae5e1-60b7-400f-94b4-6acaf6af6fd2)