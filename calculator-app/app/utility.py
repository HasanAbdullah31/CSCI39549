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
