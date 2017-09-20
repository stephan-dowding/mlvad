#!/bin/bash

brew bundle
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
