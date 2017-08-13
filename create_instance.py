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
import random
import argparse


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
Windows_Initial_Id = "ami-7da4ab6b"
Windows_Instance_Id = "ami-2f250c4f"
Linux_Instance_Id = "ami-9ec9e1fe"
Linux_Initial_Id = "ami-cd0f5cb6"

Instance_Type_List = ['t2.nano', 't2.micro', 't2.small', 't2.medium', 't2.large', 't2.xlarge', 't2.2xlarge']


class Instance():

    def __init__(self):
        print('starting to create instance randomly.')

    def write_info(self, data):
        """
        Save Instance information by json format.
        :return: 
        """
        with open('InstanceInfo.txt', 'w') as outfile:
            for item in data:
                outfile.writelines(item + '\n')

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
        if os.path.isfile('KEY_FILES/SimulatorNew.pem'):
            return

        with open('KEY_FILES/SimulatorNew.pem', 'w') as keyfile:
            key_pair = ec2_resource.create_key_pair(KeyName='SimulatorNew')
            key_pair_out = str(key_pair.key_material)
            keyfile.write(key_pair_out)

    def decrypt(self, ciphertext, keyfile=os.path.expanduser('KEY_FILES/SimulatorNew.pem')):

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
        json_data = []
        response = ec2_client.describe_instances()
        # Get all the instances and search for the instance based on the provided Tag - Name
        for reservation in response["Reservations"]:

            for item in reservation["Instances"]:
                try:
                    password_data = ec2_client.get_password_data(InstanceId=item["InstanceId"])
                    print('Password Data: {}'.format(password_data))
                    self.win_pwd = self.decrypt(password_data['PasswordData'].decode('base64'))
                    json_data.append(json.dumps({'id': item["InstanceId"],
                                                'type': item['InstanceType'],
                                                'winpwd': self.win_pwd,
                                                'public_ip': item['PublicIpAddress']}))
                except Exception as e:
                    print('Create Instance => Got Error: {}'.format(e))
                    json_data = []
                    # json_data.append(json.dumps({'id': item["InstanceId"],
                    #                              'type': item['InstanceType'],
                    #                              'winpwd': self.win_pwd,
                    #                              'public_ip': item['PublicIpAddress']}))
        if len(json_data) != 0:
            print "Writing json_data"
            self.write_info(json_data)

    def create_multi_instances(self, Image_flag=True, Window_Image=True, Linux_Image=False,
                               MinCount=1, MaxCount=1, Key_Name="SimulatorNew",
                               SubnetId='subnet-838ef8d9', **kwargs):
        """
        Create multi instances with Testkey file.
        :param num: 
        :return: 
        """
        global Instances

        if Image_flag and Window_Image:
            Image_Id = Windows_Initial_Id
        elif Image_flag and Linux_Image:
            Image_Id = Linux_Initial_Id
        elif Window_Image:
            Image_Id = Windows_Instance_Id
        else:
            Image_Id = Linux_Instance_Id

        try:
            for i in range(0, MaxCount):
                # instance_type = random.choice(Instance_Type_List)
                instance_type = 't2.medium'
                Instances = ec2_resource.create_instances(
                    ImageId=Image_Id,
                    InstanceType=instance_type,
                    MinCount=1,
                    MaxCount=1,
                    KeyName=Key_Name,
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


def start():
    """
    Entry point function
    :return: 
    """
    # Input Argument ("source image path and output path")
    ap = argparse.ArgumentParser(description='creating EC2 instance randomly for Linux or Window.')
    ap.add_argument("-w", "--window", help="Create window Instance", action="store_true")
    ap.add_argument("-l", "--linux", help="Create Linux Instance", action="store_true")
    ap.add_argument("-f", "--first", help="when use to make first instance", action="store_true")
    ap.add_argument("-n", "--number", default='1', help="The number of instances you want to make")
    ap.add_argument("-c", "--credentials", help="credentials for remote access to window instance.",
                    action="store_true")
    ap.add_argument("-t", "--terminate", help="credentials for remote access to window instance.",
                    action="store_true")
    args = vars(ap.parse_args())
    print('args: {}'.format(args))
    instance = Instance()

    if args["credentials"]:
        instance.decrypt_ec2_secure_info()

    elif args["terminate"]:
        instance.terminate_multi_instances()
    else:
        instance.create_key()
        instance.create_multi_instances(Image_flag=args["first"], Window_Image=args["window"], Linux_Image=args["linux"], MaxCount=int(args['number']))


if __name__ == '__main__':
    start()