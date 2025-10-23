#!/bin/python3
import os 

users = [ str.strip() for str in input("Input users you want to add: ").split(",") ]
        
for user in users:
    os.system(f"adduser {user}") 

        