#!/usr/bin/python
import boto3

ec2 = boto3.resource('ec2')
ec2.create_instances(ImageId='ami-fe5b6790', MinCount=1, MaxCount=1)
