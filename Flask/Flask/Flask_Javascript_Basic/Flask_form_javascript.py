#Python Lab: 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('hello.html')

@app.route('/', methods=['POST'])
def my_form_post():
    n1 = request.form['num1']
    n2 = request.form['num2']
    processed_text = int(n1)+ int(n2)
    return str(processed_text)