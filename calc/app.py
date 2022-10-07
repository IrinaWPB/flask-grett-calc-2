from flask import Flask, request
from operations import add, mult, sub, div

app = Flask(__name__)

oper_list = {
    'add': add,
    'sub': sub, 
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def calc(operation):
    """Gets a and b and returns result of calculation"""
    
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{oper_list[operation](a,b)}'
