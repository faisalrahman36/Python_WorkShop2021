from flask import Flask
'''
In order to use packages like numpy. Make sure you are using the correct environment.

To avoid the package confusion. Run command prompt from canopy.
Steps:
Run Enthought canopy as administrator.
Click Tools from top bar or the canopy editor.
Click on command prompt.
It will open the command promet with your canopy version of python with all the packages installed.

'''
#import numpy as np
app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return "<h1>Hello World</h1>  <br> ISPA Flask Lab. <h2> This is our first flask code </h2> These are some changes."

@app.route('/name/<myname>')  #myname will be any string you will pass as value. Here it will pass the folder name as variable.
def PrintValues(myname):
    '''
    You can use single quotes or double quotes like normal string.
    {} will work as place holder for myname variable.
    '''
    #x=np.linspace(1,10,num=20)
    x=[0,1,2,3]
    return '<h1 style="background-color:DodgerBlue;"> Print Values by {}</h1> <br> {} <br> This is only first value {}. <br> ISPA Flask Lab.'.format(myname,x,x[2])