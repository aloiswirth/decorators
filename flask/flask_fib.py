from flask import Flask

app = Flask(__name__)

@app.route('/')
def print_fib():
    return '<h1>Fibonacci</h1>'

@app.route('/fib')
def list_fib():
    return '<b>1, 1, 2, 3, 5, 8, 13, 21 ...</b>'

@app.route('/alo')
def list_alo():
    return '<b>It works like this as well</b>'
