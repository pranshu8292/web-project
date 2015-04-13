from flask import Flask,request,render_template

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt,mpld3

from pylab import *


#from routes import * error if i put it here

app=Flask(__name__)
'''from routes import *'''



    
    
@app.route('/hul/',methods=['GET','POST'])
def hello_world():
    
    if request.method=='GET':

        return render_template('operations.html')
    elif request.method=='POST':
        var=request.form['var']
        var=var.replace(',',"")
        
        var=[float(i) for i in var]
        cpvar=var
        sumi=sum(var)
        avg=sumi/len(var)
        prod=reduce(lambda x, y: x*y, var)
        
        
        return render_template('operations.html',sumi=sumi,avg=avg,prod=prod,cpvar=cpvar)
        
    
    else:
        return 'Invalid Request'
        


#shutting down server
@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
  
if __name__ == '__main__':
  app.run(debug=True)