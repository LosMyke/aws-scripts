#!/anaconda/bin/python

#import requests
import boto3

'''
r = requests.get('https://icanhazip.com')
puterIp = r.text
'''

client = boto3.client('ec2')
response = client.authorize_security_group_ingress(
    DryRun=False,
    GroupId='<SG>'
    #SourceSecurityGroupName='string',
    #SourceSecurityGroupOwnerId='string',
    IpProtocol='tcp',
    FromPort=22,
    ToPort=22,
    CidrIp='<IP>'
)

#print puterIp
print response

