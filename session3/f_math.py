import random
import calc
# from calc import eval
x = random.randint(0,20)
y = random.randint(0,20)
error = random.randint(-2,2)
op = random.choice(["+","-","*","/"])
r = calc.eval(x,y,op)  + error

print(x, op, y, "=", r)
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

    