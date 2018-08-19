#!/usr/bin/env bash
source ./venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=main.py
flask db downgrade 1> /dev/null
flask db upgrade 1> /dev/null
flask run