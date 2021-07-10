from flask import Flask
app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return "<h1>Hello World</h1>  <br> ISPA Flask Lab. <h2> This is our first flask code </h2> These are some changes."