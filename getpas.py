"""
getpass() prompts the user for a password without echoing.
The getpass module provides a secre way to handle the
password prompts where programs interact with the users
via the terminal

getuser() functions displays the login name of the user.
The function checks te environment variables LOGNAME,
USER,LNAME and USERNAME, in order, and returns
the value of the first non=empty string.

"""

# import getpass
# db_pass=getpass.getpass()
# print(f"Dbpassword is {db_pass}")

import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-07ebfd5b3428b6f4d',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='devops'
 )
