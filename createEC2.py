#!/usr/bin/python
import boto3

if len(sys.argv) < 3:
    print "\n============================"
    print "Error: Need to pass in AWS keys."
    print "============================\n"
    sys.exit()

print('Loading function')

# Check if even need to pass in the keys if running the function from my public VPC, might not be necessary
client = boto3.client(
  'ec2',
  aws_access_key_id=sys.argv[1],
  aws_secret_access_key=sys.argv[2]
  )

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance('oneclick')

    ec2.create_instances(
        ImageId='ami-2051294a', 
        MinCount=1,
        MaxCount=1,
        KeyName='keren-publicAWS',
        UserData=user_data,
        InstanceType='t1.micro',
        EbsOptimized=False,
        Monitoring=False
    )


    user_data = ("""
        #!/bin/bash
        git clone https://github.com/ktseytlin/OneClickDeployment.git
        cd reactServer
        # download dependencies
        npm install
        # start server
        npm run start
    """)
