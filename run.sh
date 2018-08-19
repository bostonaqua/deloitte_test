#!/usr/bin/env bash
source ./venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=main.py
flask db downgrade
flask db upgrade
flask run