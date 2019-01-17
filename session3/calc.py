def eval(x, y, pheptinh):
    result = 0
    if pheptinh == "+":
        result = x + y
    elif pheptinh == "*":
        result = x * y
    elif pheptinh == "-":
        result = x - y
    else: 
        result = x / y
    return result

