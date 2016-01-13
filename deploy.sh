#!/bin/bash

DEPLOY_ENV=$1

# setup ansible locally if it does not exist
if ! type "ansible" > /dev/null; then
    sudo pip install ansible
fi

# for testing:
# ansible all -i hosts.ini --module-name ping -u ubuntu

ansible-playbook -i hosts.ini playbooks/bkpm.yml -e "env=${DEPLOY_ENV}" #-vvvv