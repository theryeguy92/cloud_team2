#!/bin/bash

# Define the bastion server
BASTION_USER="cc"
BASTION_IP="129.114.27.250"
BASTION_KEY="~/.ssh/F24_BASTION.pem"

# Define the target server
TARGET_USER="cc"
TARGET_IP="192.168.5.102"
TARGET_KEY="~/.ssh/Assignment1.pem"

# Execute the SSH connection using the bastion server as a proxy
ssh -o ProxyCommand="ssh -i $BASTION_KEY -W %h:%p $BASTION_USER@$BASTION_IP" -i $TARGET_KEY $TARGET_USER@$TARGET_IP