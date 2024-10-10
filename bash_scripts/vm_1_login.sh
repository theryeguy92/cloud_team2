#!/bin/bash

# Define the server (Just plug in the IP)
BASTION_USER="cc"
BASTION_IP="129.114.27.250"
BASTION_KEY="~/.ssh/F24_BASTION.pem"

# Target server
TARGET_USER="cc"
TARGET_IP="192.168.5.134"
TARGET_KEY="~/.ssh/Assignment1.pem"

# Execute the SSH connection
ssh -o ProxyCommand="ssh -i $BASTION_KEY -W %h:%p $BASTION_USER@$BASTION_IP" -i $TARGET_KEY $TARGET_USER@$TARGET_IP