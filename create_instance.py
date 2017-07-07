import boto3
import json
import os
import sys

"""
Create EC2 instance randomly.
"""

with open('credentials.json') as credentials_file:
    data = json.load(credentials_file)

ec2_resource = boto3.resource('ec2',
                              aws_access_key_id=data["AWS_ACCESS_KEY"],
                              aws_secret_access_key=data["AWS_SECRET_KEY"],
                              region_name=data["AWS_REGION"])

ec2_client = boto3.client('ec2',
                          aws_access_key_id=data["AWS_ACCESS_KEY"],
                          aws_secret_access_key=data["AWS_SECRET_KEY"],
                          region_name=data["AWS_REGION"])
Instances = []


def create_key():
    """
    Create the EC2 key file
    :return: 
    """
    if os.path.isfile('KEY_FILES/Windowskey.pem'):
        return

    with open('KEY_FILES/Windowskey.pem', 'w') as keyfile:
        key_pair = ec2_resource.create_key_pair(KeyName='Windowskey')
        key_pair_out = str(key_pair.key_material)
        keyfile.write(key_pair_out)


def create_multi_instances(Image_Id="ami-a0260bc0", Instance_Type="t2.micro",
                           MinCount=1, MaxCount=1, Key_Name="Windowskey", SubnetId='subnet-6acf8d32',
                           **kwargs):
    """
    Create multi instances with Testkey file.
    :param num: 
    :return: 
    """
    global Instances
    try:
        Instances = ec2_resource.create_instances(
            ImageId=Image_Id,
            InstanceType=Instance_Type,
            MinCount=MinCount,
            MaxCount=MaxCount,
            KeyName=Key_Name,
            SubnetId=SubnetId
        )

        # Waiting to be ready in state.
        for instance in Instances:
            while instance.state == "pending":
                print(instance, instance.state)
                instance.update()
        print(Instances)
    except Exception as e:
        print("Create multi Instances Error: {}".format(e))


def remove_multi_instances():
    """
    Terminate Instances
    :return:
    """

    ec2_client.terminate_instances(InstanceIds=Instances)


def connect_instance():
    """
    connect to instance via ssh.
    :return: 
    """

    pass


if __name__ == '__main__':
    print('starting....')
    create_key()
    create_multi_instances()
    # remove_multi_instances()
