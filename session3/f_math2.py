import random
while True:
    x = random.randint(0,20)
    y = random.randint(0,20)
    error = random.randint(-2,2)
    operator = ["+","-","*","/"]
    op = random.choice(operator)
    if op == "+":
        r = x + y  + error
    elif op == "-":
        r = x - y  + error
    elif op == "*":
        r = x * y  + error
    else:
        r = x / y  + error
    print(x,op,y,"=",result)
    answer = input("Y/N:")

    result = None
    if answer == "y":
        if error == 0:
            result = "Yay"
        else :
            result = "Nay"
    if answer == "n":
        if error != 0:
            result = "Yay"
        else :
            result = "Nay"
    
    print(result)