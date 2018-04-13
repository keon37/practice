from flask import Flask, render_template, redirect, flash, request, url_for
# from flask import Flask, render_template, request 
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('signup.html')

@app.route('/success/<name>')
def success(name=None):
    retunr render_template('success.html', name = name)
    # return  'Main page %s ' % name

@app.route('/login', methods=['GET' , 'POST'])
def signup ():
     if request.method == 'POST':
      user = request.form['myName']
      print("user :" + user)
      return redirect(url_for('success', name = user))

    # if request.method == 'POST' :
    #     request.form


if __name__ =='__main__':
    app.debug=True
    app.run()