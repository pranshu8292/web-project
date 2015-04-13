from flask import Flask,request,render_template

app=Flask(__name__)
'''from routes import *'''
@app.route('/personal')
def index():
    return render_template("personal.html")    
@app.route('/base')   
def index1():
    return render_template("base.html")  
@app.route('/base1')   
def index2():
    return render_template("base1.html")    

@app.route('/base2')   
def index3():
    return render_template("base2.html")

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

