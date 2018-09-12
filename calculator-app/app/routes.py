# Page routes

from app import app
from .utility import get_result
from .calculator import Calculator

calc = Calculator()
add_instr = 'To add the numbers x and y, go to the endpoint /add/x/y'
sub_instr = 'To subtract the numbers x and y, go to the endpoint /subtract/x/y'
mul_instr = 'To multiply the numbers x and y, go to the endpoint /multiply/x/y'
div_instr = 'To divide the numbers x and y, go to the endpoint /divide/x/y'

@app.route('/')
@app.route('/index')
def index():
    return ('Hello, world! This is my calculator app.' +
            '<ul>' +
            f'<li>{add_instr}</li>' +
            f'<li>{sub_instr}</li>' +
            f'<li>{mul_instr}</li>' +
            f'<li>{div_instr}</li>' +
            '</ul>')

@app.route('/add')
def add_default():
    return f'This is the default add page.<br>{add_instr}'

@app.route('/add/<x>/<y>')
def add(x, y):
    return get_result(x, y, '+', calc.add)

@app.route('/subtract')
def subtract_default():
    return f'This is the default subtract page.<br>{sub_instr}'

@app.route('/subtract/<x>/<y>')
def subtract(x, y):
    return get_result(x, y, '-', calc.subtract)

@app.route('/multiply')
def multiply_default():
    return f'This is the default multiply page.<br>{mul_instr}'

@app.route('/multiply/<x>/<y>')
def multiply(x, y):
    return get_result(x, y, '*', calc.multiply)

@app.route('/divide')
def divide_default():
    return f'This is the default divide page.<br>{div_instr}'

@app.route('/divide/<x>/<y>')
def divide(x, y):
    return get_result(x, y, '/', calc.divide)
