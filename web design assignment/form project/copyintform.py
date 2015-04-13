from flask import Flask,request,render_template

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt,mpld3
import os
from pylab import *


#from routes import * error if i put it here

app=Flask(__name__)
'''from routes import *'''

w,b=0,0

@app.route('/index/',methods=['GET','POST'])
def index():
    return render_template("home.html")    
    
@app.route('/gul/',methods=['GET','POST'])
def hello_world():
    
    if request.method=='GET':
        
        return render_template('cform.html')
    elif request.method=='POST':
        global w,b
        w=w+1
        b=b+1
        llimit=float(request.form['llimit'])
        ulimit=float(request.form['ulimit'])
        func=request.form['func']
        func=eval(func)
        #val=func(3.14)
        div=int(request.form['div'])
        simarea=simpson(func,llimit,ulimit,div)
        traparea=trape(func,llimit,ulimit,div)
        simplot(func,llimit,ulimit,div)
        traplot(func,llimit,ulimit,div)
        return render_template('cform.html',simarea=simarea,traparea=traparea)
        
    
    else:
        return 'Invalid Request'


@app.route('/hul/',methods=['GET','POST'])
def hello_worl():
    
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
        
#plotting the graph with simplot
def simplot(f,a,b,n):
    g=0
    x=np.arange(a,b,0.1)
    y=f(x)
    plt.plot(x,y,'r-')
    z=np.linspace(a,b,n)#divide interval in n parts
    g,h=[],[]
    i=0
    while i<len(z)-1:
        g.append((z[i]+z[i+1])/2.0)
        i=i+1
        
    for i in g:
        h.append(f(i))#corresponding y cordinates
    w=z[1]-z[0]#width
    
    v=z
    v=np.delete(v,len(v)-1)#delete the last cordinate
    plt.bar(v,h,width=w)
    for i,j in zip(g,h):
        plt.plot([i,i],[j,0],'r--')
    plt.title('INTEGRATION BY SIMPSONS METHOD')
    plt.xlabel('X-AXIS')
    plt.ylabel('Y-AXIS')
    
    plt.savefig('C:/Users/hp/Desktop/form project/static/img/dev.png', bbox_inches='tight')
  
    
    plt.clf()
   

#plotting by traplot
                
def traplot(f,a,b,n):
     x=np.arange(a,b,0.1)
     y=f(x)
     plt.plot(x,y,'r-')
     z=np.linspace(a,b,n)
     y=[0]*n
     plt.plot(z,y,'bo-')
     plt.plot(z,f(z),'bo')
     c=f(z)
     for i,j in zip(z,c):
         plt.plot([i,i],[j,0],'bo-')
     plt.plot(z,f(z),'bo-')
     plt.fill_between(z,c, color='green')
     plt.title('INTEGRATION BY TRAPEZOIDAL METHOD')
     plt.xlabel('X-AXIS')
     plt.ylabel('Y-AXIS')
     plt.savefig('C:/Users/hp/Desktop/form project/static/img/noo.png', bbox_inches='tight')
    
     
     plt.clf()
    

#integration by simpsons  method
def simpson(f,a,b,n):
        x=np.linspace(a,b,n+1)
        y=f(x)
    
        h = float(x[1] - x[0])
        n = len(x) - 1
        if n % 2 == 1:
            n -= 1
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        return h * s / 3.0
        
#integration with trapezoidal method
def trape(f,a,b,n):
    
    x=np.linspace(a,b,n+1)
    y=f(x)
    s=y[0]+2.0*sum(y[1:n])+y[n]
    h=float(b-a)/n
    return s*h/2.0

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


