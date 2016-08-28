#!/usr/bin/python
import boto3

if len(sys.argv) < 3:
    print "\n============================"
    print "Error: Need to pass in AWS keys."
    print "============================\n"
    sys.exit()

client = boto3.client(
  'ec2',
  aws_access_key_id=sys.argv[1],
  aws_secret_access_key=sys.argv[2]
  )

ec2 = boto3.resource('ec2')
instance = ec2.Instance('oneclick')

ec2.create_instances(
  ImageId='ami-fe5b6790', 
  MinCount=1,
  MaxCount=1,
  KeyName='',
  SecurityGroups=['',],
  UserData=user_data,
  InstanceType='t1.micro',
  IamInstanceProfile={
    'ARN': '',
    'Name': ''
    },
  EbsOptimized=False,
  Monitoring=False
  )


user_data = (
  #!/bin/bash
  git clone https://github.com/ktseytlin/OneClickDeployment.git
  cd reactServer
  # download dependencies
  npm install
  # start server
  npm run start
  )
