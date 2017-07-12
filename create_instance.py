import boto3
import json
import os
import sys
import winrm
import crypto
sys.modules['Crypto'] = crypto
from crypto.Cipher import PKCS1_v1_5
from crypto.PublicKey import RSA
import time
import paramiko

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


class Instance():

    def __init__(self):
        print('starting to create instance randomly.')

    def write_info(self, data):
        """
        Save Instance information by json format.
        :return: 
        """

        with open('InstanceInfo.txt', 'w') as outfile:
            outfile.writelines(data + '\n')

    def read_info(self):
        """
        Read Information from InstanceInfo.txt file.
        :return: 
        """
        with open('InstanceInfo.txt', 'r') as outfile:
            data = outfile.readlines()
            return data

    def create_key(self):
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

    def decrypt(self, ciphertext, keyfile=os.path.expanduser('KEY_FILES/Windowskey.pem')):

        input = open(keyfile)
        key = RSA.importKey(input.read())
        input.close()
        cipher = PKCS1_v1_5.new(key)
        plaintext = cipher.decrypt(ciphertext, None)
        return plaintext

    def decrypt_ec2_secure_info(self):
        """
        Get windows password and save information to InstanceInfo.txt file.
        """
        response = ec2_client.describe_instances()
        # Get all the instances and search for the instance based on the provided Tag - Name
        for reservation in response["Reservations"]:
            for item in reservation["Instances"]:
                print('Instance {}'.format(item))
                password_data = ec2_client.get_password_data(InstanceId=item["InstanceId"])
                print('Password Data: {}'.format(password_data))
                win_pwd = self.decrypt(password_data['PasswordData'].decode('base64'))
                self.write_info(json.dumps({'id': item["InstanceId"],
                                            'type': item['InstanceType'],
                                            'winpwd': win_pwd,
                                            'public_ip': item['PublicIpAddress']}))

    def create_multi_instances(self, Image_Id="ami-b4614cd4", Instance_Type="t2.micro", MinCount=1,
                               MaxCount=1, Key_Name="Windowskey", SubnetId='subnet-6acf8d32', **kwargs):
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

        except Exception as e:
            print("Create multi Instances Error: {}".format(e))

    def terminate_multi_instances(self):
        """
        Terminate Instances
        :return:
        """
        instances = self.read_info()

        for item in instances:
            instance_item = ec2_resource.Instance(json.loads(item)['id'])
            response = instance_item.terminate()
            print response

        with open('InstanceInfo.txt', "w"):
            pass

if __name__ == '__main__':
    instance = Instance()
    # instance.create_key()
    # instance.create_multi_instances()
    instance.decrypt_ec2_secure_info()
    # instance.terminate_multi_instances()