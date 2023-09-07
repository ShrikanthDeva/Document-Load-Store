import csv

def get_credentials():
    with open("./commvault-user_accessKeys.csv", 'r') as file:
        csvreader = list(csv.reader(file))
        data = csvreader[1]
        credentials = {'AccessKey': data[0], "SecertAccessKey": data[1]}
        # print(credentials)
        return credentials
  


        