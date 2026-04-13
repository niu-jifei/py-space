#!/bin/bash


# 1. Create virtual environment
if [ ! -d .venv ]; then
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
#   deactivate
fi


# 2. Activate virtual environment
source .venv/bin/activate

# 3. Deactivate virtual environment
# deactivate
