#!/bin/bash

# Package server application
# pip install -e .
# python3 application/setup.py sdist

# Copy package
# mv dist/redfish-0.1.tar.gz roles/redfish/files/redfish-0.1.tar.gz

# Clean temp build files
# rm -rf build dist redfish.egg-info

# Deploy via Ansible
ansible-playbook playbook.yml -i inventory

# Run functionnal tests
python3 -m pytest tests/
