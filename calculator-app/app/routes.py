# Page routes

from app import app

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

calculator = Calculator()

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! This is my calculator app."

@app.route('/add')
def add():
    return "1 + 2 = .... " + str(calculator.add(1,2))

@app.route('/subtract')
def subtract():
    return "1 - 2 = .... " + str(calculator.subtract(1,2))

@app.route('/multiply')
def multiply():
    return "1 * 2 = .... " + str(calculator.multiply(1,2))

@app.route('/divide')
def divide():
    return "1 / 2 = .... " + str(calculator.divide(1,2))
