import flask
import os
import operator
from flask import Flask, flash, redirect, render_template, request, session, abort
import subprocess

app = Flask(__name__)


with open("savedata.txt", "r") as fo:
            variable = int(fo.read())
            
@app.route('/startseite')
def home():
    global variable
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html', variable= variable)

@app.route('/', methods=['GET','POST'])
def start():
    global variable
    return render_template('startseite.html', variable = variable)


@app.route('/login', methods=['GET','POST'])
def do_admin_login():
    login = request.form
  
    global variable
    if "plus20" in request.form:
        
            variable +=20
            with open("savedata.txt", "w") as fo:
               fo.write(str(variable))
            print("download"+str(variable))
            return home()
    if "plus10" in request.form:
        
            variable +=10
            with open("savedata.txt", "w") as fo:
               fo.write(str(variable))
            print("download"+str(variable))
            return home()
    if "plus5" in request.form:
        
            variable +=5
            with open("savedata.txt", "w") as fo:
               fo.write(str(variable))
            print("download"+str(variable))
            return home()
    if "minus20" in request.form:
        
            variable -=20
            with open("savedata.txt", "w") as fo:
               fo.write(str(variable))
            print("download"+str(variable))
            return home()
    if "minus10" in request.form:
        
            variable -=10
            with open("savedata.txt", "w") as fo:
               fo.write(str(variable))
            print("download"+str(variable))
            return home()
    if "minus5" in request.form:
        
            variable -=5
            with open("savedata.txt", "w") as fo:
               fo.write(str(variable))
            print("download"+str(variable))
            return home()

    userName = login['username']
    password = login['password']

    p = subprocess.Popen(['python', 'test.py', userName, password], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print('out', out)
    print('err', err)
    print('returncode', p.returncode)
    print('EXIT')
    out = str(out)
    if(out.find('tritt') != -1 ):
        print("erfolg")
        session['logged_in'] = True
    else:
        print("fehler")
        flash('wrong password!')

    
    
    return home()

@app.route('/logout')
def logout():
  session['logged_in'] = False
  return home()

if __name__ == "__main__":
  app.secret_key = os.urandom(12)
  app.run(debug=False,host='0.0.0.0', port=5000)






