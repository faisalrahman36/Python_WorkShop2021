#I used Flask2.py as name which is a bad practice but just to show it is different from giving flask.py and will work. 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return "<h1>Hello World</h1>  <br> ISPA Flask Lab. <h2> This is our first flask code </h2> These are some changes."

@app.route('/<myname>')  #myname will be any string you will pass as value. Here it will pass the folder name as variable.
def HelloWorld_withname(myname):
    ''' 
    You can use single quotes or double quotes like normal string.
    {} will work as place holder for myname variable.
    '''
    return '<h1>Hello World by {}</h1>  <br> ISPA Flask Lab.'.format(myname)
    
'''

When you will run it like this http://127.0.0.1:5000/

This won't work as you have added <myname> in your app.route decorator so you will need to write

For more information on decorators, read: https://realpython.com/primer-on-python-decorators/#simple-decorators

For more on HTML , https://www.w3schools.com/html/

For Flask, https://flask.palletsprojects.com/en/1.1.x/quickstart/
https://www.tutorialspoint.com/flask/flask_variable_rules.htm


'''