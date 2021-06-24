import os
from flask import Flask, render_template, send_from_directory, json, request 
from dotenv import load_dotenv
from . import db 

load_dotenv()

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite') 
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/health')
def health():
    return render_template('health.html', url=os.getenv("URL"))
