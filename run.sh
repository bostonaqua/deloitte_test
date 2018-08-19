#!/usr/bin/env bash
export FLASK_APP=main.py
flask db downgrade 2> /dev/null
flask db upgrade 2> /dev/null
flask run
