from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello world"

@app.route('/maxes')
def maxes():
    return render_template('max.html')