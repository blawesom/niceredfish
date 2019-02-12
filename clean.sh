#!/bin/bash

rm -r .pytest_cache
rm step*/__pycache__/*
rmdir step*/__pycache__
rm step*/tests/__pycache__/*
rmdir step*/tests/__pycache__
rm step*/*.retry
rm -r step*/roles/redfish/files/build/*
rmdir step*/roles/redfish/files/build
rm -r step*/roles/redfish/files/dist/*
rmdir step*/roles/redfish/files/dist
rm -r step*/roles/redfish/files/*egg*/*
rmdir step*/roles/redfish/files/*egg*
