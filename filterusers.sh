#!/bin/bash
touch ~ /Script.log 
echo > ~/Script.log
chmod 777 ~/Script.log

echo "Script Log created"

mkdir -p ~/backups

echo "Backups directory created"

cp /etc/passwd ~/backups/

echo "/etc/passwd file backed up"