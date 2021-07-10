from flask import Flask
import numpy as np
app=Flask(__name__)

@app.route('/<myname>')
def Flask16June(myname):
    x=np.linspace(10,50,num=20)
    tx=type(x).__name__
    return '<h1 style="background-color:DodgerBlue;color:Red;" >Hello World</h1> <p style="color:DodgerBlue;"> ISPA Python Class </p><br/><h2> {} </h2> <br/> {} <br/> This will print only first value: {} -- %s<br/> '.format(myname,x,x[0]) %tx