#!/usr/bin/env bash
source ./venv/bin/activate
pip install -r requirements.txt 1> /dev/null
export FLASK_APP=main.py
flask db downgrade 2> /dev/null
flask db upgrade 2> /dev/null
flask run