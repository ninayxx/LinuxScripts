#!/bin/bash
touch ~/Script.log
chmod 777 ~/Script.log

echo "Script Log created"

mkdir -p ~/backups

echo "Backups directory created (/root/backups)" > ~/Script.log 

cp /etc/passwd ~/backups/

echo "/etc/passwd file backed up"

echo "/etc/passwd file backed up" > ~/Script.log