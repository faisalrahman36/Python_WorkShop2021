#Python Lab: 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('hello.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    #processed_text = int(text)+3
    processed_text = text.upper() +'some text'
    return str(processed_text)