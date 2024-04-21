#!/usr/bin/python3

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return 'Hello, {}!'.format(escape(name))
