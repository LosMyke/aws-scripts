#!/usr/bin/python

import boto3
import json

elb  = raw_input("Enter ELB name: ")

client = boto3.client('elb')



response = client.describe_instance_health(
    ### Modify below to the name of your ELB
    LoadBalancerName=elb,
    )


print "############################"
print "######### All Instances ####"
print "############################"

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


