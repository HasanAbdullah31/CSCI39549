# Useful functions

def str_to_num(x):
    try:
        if int(x) == float(x):
            return int(x)
    except ValueError:
        # assert: x is either a string of a float or a string of chars
        try:
            return float(x)
        except ValueError:
            # assert: x is a string of chars
            raise ValueError('string could not be converted to a number')

def get_result(x, y, sign, func):
    try:
        x = str_to_num(x)
        y = str_to_num(y)
        return f'{x} {sign} {y} = {func(x,y)}'
    except ValueError as err:
        return f'There was an error with the inputs ({err}). Try again.'
    except ZeroDivisionError:
        return 'Cannot divide by zero! Try again.'
