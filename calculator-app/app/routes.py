# Page routes

from app import app
from .calculator import Calculator

calc = Calculator()

@app.route('/')
@app.route('/index')
def index():
    return ("Hello, World! This is my calculator app."+
            "<ul>"+
            "<li>To add, go to the endpoint /add</li>"+
            "<li>To subtract, go to the endpoint /subtract</li>"+
            "<li>To multiply, go to the endpoint /multiply</li>"+
            "<li>To divide, go to the endpoint /divide</li>"+
            "</ul>")

@app.route('/add')
def add():
    return "1 + 2 = .... " + str(calc.add(1,2))

@app.route('/subtract')
def subtract():
    return "1 - 2 = .... " + str(calc.subtract(1,2))

@app.route('/multiply')
def multiply():
    return "1 * 2 = .... " + str(calc.multiply(1,2))

@app.route('/divide')
def divide():
    return "1 / 2 = .... " + str(calc.divide(1,2))
