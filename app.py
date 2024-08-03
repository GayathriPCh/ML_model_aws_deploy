from flask import Flask, request
app = Flask(__name__) #is a constructor
@app.route('/') # is a decorator
def hello(): # type: ignore
	return 'hello'
@app.route('/predictor')
def ppd():
    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    ps = request.form.get('ps')

