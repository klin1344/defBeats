
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, url_for, request, render_template
import os
from collections import Counter

app = Flask(__name__, template_folder=os.path.dirname(__file__))

@app.errorhandler(Exception)
def all_exceptions(error):
    return 'man, you really fucked up', 500

@app.errorhandler(500)
def shits_fucked(e):
    return 'shits fucked, son'


@app.route('/')
def friggingdone():
    return render_template('index.html')


