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
### home page 
![image](./Images/Home-page.png)
### upload page
![image](Images/upload-1.png)
![image](Images/upload-2.png)
![image](Images/upload-3.png )
### search page
![image](Images/Search-1.png)
+ FOUND CASE
![image](Images/Search-2.png)
![image](Images/Search-3.png)
+ NOT FOUND CASE
![image](Images/Search-4.png)
![image](Images/Search-5.png)
### Download page
![image](Images/Download-1.png)
+ FOUND CASE
![image](Images/Download-2.png)
![image](Images/Download-3.png)
+ NOT FOUND CASE
![image](Images/Download-4.png)
![image](Images/Download-5.png)


### EC2 INSTANCE
![image](Images/Ec2-on-aws.png)

### S3 BUCKET
![image](Images/S3-bucket.png)

### IAM USER FOR seprate user not using root user for confidential purpose
![image](Images/IAM-1.png)

![image](Images/IAM-2.png)


# DEPLOYMENT
+ could locally run the application on the ec2 instance but not deploy it
![image](Images/App-on-EC2.png)