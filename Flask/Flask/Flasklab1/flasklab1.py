#Flask Lab
from flask import Flask
app = Flask(__name__)


@app.route('/')
def mainpage():
   return 'Main page'
   
@app.route('/squareint/<int:num>')
def squareint(num):
   tn=type(num).__name__
   return 'Square of number %d is %d. Data type is : %s ' % (num,num**2,tn)

@app.route('/squarefloat/<float:fnum>')
def squarefloat(fnum):
   tf=type(fnum).__name__
   return 'Square of number %f is %f. Data type is :{}'.format(tf) % (fnum,fnum**2)
   
   