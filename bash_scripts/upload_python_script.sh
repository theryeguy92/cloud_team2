#!/bin/bash

# Define the bastion server
BASTION_USER="cc"
BASTION_IP="129.114.27.250"
BASTION_KEY="/home/ryan/.ssh/F24_BASTION.pem"

# Define the target server
TARGET_USER="cc"
TARGET_IP="192.168.5.134"
TARGET_KEY="/home/ryan/.ssh/Assignment1.pem"

# Define the source and destination paths
SOURCE_FILE="/home/ryan/Apps/python/iot_producer.py"
DESTINATION_PATH="/home/cc/"

# Execute the SCP command using the bastion server as a proxy
scp -o ProxyCommand="ssh -i $BASTION_KEY -W %h:%p $BASTION_USER@$BASTION_IP" -i $TARGET_KEY $SOURCE_FILE $TARGET_USER@$TARGET_IP:$DESTINATION_PATH