#!/bin/bash

rm -r .pytest_cache
rm step*/__pycache__/*
rmdir step*/__pycache__
rm step*/tests/__pycache__/*
rmdir step*/tests/__pycache__
rm step*/*.retry