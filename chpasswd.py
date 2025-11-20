#!/bin/python3
import os 

users = [ str.strip() for str in input("Input users with insecure passwords: ").split(",") ]

os.system(f"touch ~")

for user in users:

    os.system(f"echo -e 'P1ssw0rd5892!!\nP1ssw0rd5892!!' | passwd {user}") 