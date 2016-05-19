#!/usr/bin/python

import boto3
import json

client = boto3.client('elb')

response = client.describe_instance_health(
    LoadBalancerName='elb-test-1',
    )

for output in response['InstanceStates']:
		instState = output['State']
		instId = output['InstanceId']
		print("%s - %s" % (instId, instState))

print "############################"
print "####### OutOfService Only ##"
print "############################"

for oos in response['InstanceStates']:
		if oos['State'] == "OutOfService":
			instState = oos['State']
			instId = oos['InstanceId']
			print("%s - %s" % (instId, instState))


