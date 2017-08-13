# Simulate-User-Activity
Create a python script to simulate user activity on aws ec2.

# Directory Structure.

- automate_lib : Includes base functions to process with windows handler and browser.
- KEY_FILES : Includes *.pem file for EC2 instance.
- create_instance.py : This file is used to create/terminate/get password for EC2 generated programmatically.

    * Parameters: -f, -w, -l -m
        
        * -f: when you create new first instance on the other account.
        * -w: when you create windows instance.
        * -l: when you create linux instance.
        * -m: the number of instances which you want to create at once.
        * -c: decrypt the pem file and extract credentials to InstanceInfo.txt file. (this only is used for windows instance.)
        * -t: terminate the instances.
        
- InstanceInfo.txt : This file is used to save Instance IP address and the other information for EC2 Instances running now.
- simulate.py : This file is main file to start simulate.


# Instructions to set up on new Instance.

- Step 1: 
    
    * First run the script with these parameters.
        
    ```
        python create_instance.py -f -w
    ```
       
- Step 2:
    
    This step is only for windows instance. 
    if it is created linux instance with "-l" parameter, then you can pass this step.
    
    * After 10 minutes, run below command to extract the credentials to file for accessing remote.
     
     ```
        python create_instance.py -c
     ```
     
    * afterwards, You can check instanceInfo.txt file to get credentials for remote desktop, 
     which includes instance ip, winpwd (password), the other infos. you can use that information to remote desktop.
       
    * Run *Remote Desktop Connection* and insert above credentials on window popping up. 
    (username is *Administrator*, password is the value of *winpwd* in InstanceInfo.txt file)

- Step 3:
    
    Assuming you are in Remote Desktop now.
    
    * Install Python2.7.exe
        open the *Internet Explorer* and search python2.7 on google, download that and run the exe file to install python 2.7
        
    * Copy source code to Instance which you made above. you can put that source code on *C://workspace* path.
    
- Step 4:    

    Set Internet Explorer security option
    
- Step 5:

    This step should be set that script would be run whenever user login.
    For this
    
    * Click the Windows *Start menu*, click *Control Panel* > *Administrative Tools* and click *Task Scheduler*.
    
    * The Actions pane, on the right, has the Create Basic Task action, and this is the place to start.
    
    * Clicking on Create Basic Task opens a wizard where you define the name of your task, the trigger (when it runs), and the action (what program to run).
    
        ** name: you can type something what you want to type (for example: simulator)
        ** trigger: select *When I log on*
        ** Action: select *Start a Program*
            *** program/script: the location of python.exe (for example: C:\Python27\python.exe)
            *** Add arguments: the location of script (for example: C:\workspace_1\simulate.py)
        
        In last step, click *Finish* button.
        
- Step 6:

    This step is to install *tightvnc* on windows instance.
    For this
    
    * Open the *Internet Explorer* and search *tightvnc* and download, Install it.
     after installed, it will be displayed the window to set password for *tightvnc*. you can set password as you want.
     I set *admin* as password. so that you can connect to instance with ip address and password via *tightvnc*.
     
# Note

After you have already set new instance,then you can snapshot this instance to create custom AMI.

We can use this custom AMI directly to create multi-instance at once.