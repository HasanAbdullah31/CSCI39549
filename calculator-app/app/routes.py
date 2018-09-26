# Page routes

from flask import request, render_template
from .utility import str_to_num
from app import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        req = request.form['req']
        try:
            x = str_to_num(request.form['x'])
            y = str_to_num(request.form['y'])
        except ValueError as err:
            return f'There was an error with the inputs ({err}). Try again.'
        if req == 'add':
            return str(x + y)
        elif req == 'sub':
            return str(x - y)
        elif req == 'mul':
            return str(x * y)
        elif req == 'div':
            try:
                return str(x / y)
            except ZeroDivisionError:
                return 'Cannot divide by zero! Try again.'
    return render_template('index.html')
