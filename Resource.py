import boto3
aws_mg_con=boto3.session.Session(profile_name="root") #custome session.
iam_con_re=aws_mg_con.resource(service_name="iam", region_name="us-east-1")
ec2_con_re=aws_mg_con.resource(service_name="ec2", region_name="us-east-1")
s3_con_re=aws_mg_con.resource(service_name="s3", region_name="us-east-1")

#list all iam users

print("list of users : ")
for each_item in iam_con_re.users.all():
	print(each_item.user_name)

print("list of buckets: ")
for each_item in s3_con_re.buckets.limit(10):
 	print(each_item.name)

print("list of ec2 instances available: ")
#each_item_all=[]
for each_item in ec2_con_re.get_available_subresources():
	    if each_item=="Instance":
	       for instance in ec2_con_re.instances.all():
	      	  print(instance.id ,instance.state)
	      	  

	   	       


       

	
		   

