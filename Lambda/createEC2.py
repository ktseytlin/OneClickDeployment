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
    # instance = ec2.Instance('oneclick')

    oneclick = ec2.create_instances(
    # need to also configure this to have a public IP - might happen by default?
        ImageId='ami-6869aa05',
        MinCount=1,
        MaxCount=1,
        KeyName='keren-publicAWS',
        UserData=user_data,
        InstanceType='t1.micro',
        EbsOptimized=False,
        Monitoring=False,
        SubnetID='subnet-1a426830',
        SecurityGroups=['sg-1ffb7065','sg-6b11a311', 'sg-b57f41ce']
    )

    user_data = ("""
        #!/bin/bash
        # ip-172-31-54-162
        # TODO: Double check through this whole bash script again, then try automating
        # sudo su -
        # sudo yum install wget -y
        sudo yum install git-core -y
        sudo yum install ruby -y
        sudo yum groupinstall 'Development Tools' && sudo yum install curl git m4 ruby texinfo bzip2-devel curl-devel expat-devel ncurses-devel zlib-devel
        # TODO: figure out how to -y in everything for that big number of things I need above

        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)"
        PATH="$HOME/.linuxbrew/bin:$PATH"
        echo 'export PATH="$HOME/.linuxbrew/bin:$PATH"' >> ~/.bash_profile
        echo 'export MANPATH="$HOME/.linuxbrew/share/man:$MANPATH"' >> ~/.bash_profile
        echo 'export INFOPATH="$HOME/.linuxbrew/share/info:$INFOPATH"' >> ~/.bash_profile

        ## Now installing node w/o brew, can we get rid of brew then? check.
        sudo su -
        curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -
        yum install -y nodejs
        yum install -y gcc-c++ make

        echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDK0z2C6oztyELw9AhgIY7ZtehQw7cBvRYKjwTGaaTP+/Uj6n+WjlYRlGJlLQxZhYENzVS+7gsNdOPhVIcn2Txrl27FarS30rDjCGs6FueP8GtpCWiFA5JVVReOZF5RgvRAzY0n9njtFIlbmoks+LkV47QQlVVnzVLIGIp9EEKk0WjbPEO8sRcK7xzjHykrHtLx26mXhNPktM7cQbNmQh7JkmpSwcLWaSqT8xYMa7Cld++7MB66pfDhs3FFd+zmfJuU8S6zfComcM3WZEOLfx8+nK2ztWMJEEZh842TFIhW5Vxf7kCMQFfJ+h6Vl3LBC6rkq9l0ZtCYEgd2ofENloHL und608@acbc32caae63" >> ~/.ssh/authorized_keys
        git clone https://github.com/ktseytlin/OneClickDeployment.git
        cd OneClickDeployment/GeneralWebAppScaffold
        # download dependencies
        npm install
        # start server
        npm run start
    """)

        oneclick.create_tags(
            Tags = [
                {
                    'Key': 'Name',
                    'Value': 'OneClickDeployment'
                },
            ]
        )

    logger.info('End of lambda function')
