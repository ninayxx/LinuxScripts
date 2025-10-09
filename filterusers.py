#!/bin/python3
import shutil
import os
from datetime import datetime

source_dir = "/etc/passwd"



orig_file = ""

with open("/etc/passwd","r") as file:
    orig_file = file.readlines()

with open("./passwd.bak", "w") as file:
    file.write(orig_file)

auth_users = [ str.strip() for str in input("Input authorized users: ").split(",") ]

buffer = ""

systemusers = []

with open("./systemusers","r") as file:
    users = file.readlines()

    for user in users:
        username = user.split(":")[0]
        systemusers.append(username)
        
with open("/etc/passwd","r") as file:
    users = file.readlines()

    for user in users:
        username = user.split(":")[0]
        if username in auth_users or username in systemusers or user.split(":")[6]=="/usr/sbin/nologin":
            buffer += user

with open("/etc/passwd", "w") as file:
    file.write(buffer)

        


        
