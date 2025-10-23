#!/bin/python3
import os 
import subprocess 

subprocess.run(["bash", "filterusers.sh"], check=True)

auth_users = [ str.strip() for str in input("Input authorized users: ").split(",") ]
        
with open("/etc/passwd","r") as file:
    users = file.readlines()

    for user in users:
        username = user.split(":")[0].strip()
        if username not in auth_users and user.split(":")[6].strip()=="/bin/bash" and user.split(":")[3] != "0":
            os.system(f"userdel -r {username} 2> /dev/null") 

        


        
