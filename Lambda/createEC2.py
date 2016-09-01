#!/usr/bin/python

# http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Subnet.create_instances

import boto3
import logging

# if len(sys.argv) < 3:
#     print "\n============================"
#     print "Error: Need to pass in AWS keys."
#     print "============================\n"
#     sys.exit()

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info('Loading function')

# Check if even need to pass in the keys if running the function from my public VPC, might not be necessary
# client = boto3.client(
#     'ec2',
#     aws_access_key_id=sys.argv[1],
#     aws_secret_access_key=sys.argv[2]
#     )

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    logger.info('In lambda function')
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
        cd GeneralWebAppScaffold
        # download dependencies
        npm install
        # start server
        npm run start
    """)

    logger.info('End of lambda function')
