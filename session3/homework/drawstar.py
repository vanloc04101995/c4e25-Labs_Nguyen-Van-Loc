from turtle import *
shape("turtle")
def draw_star(x,y,length):
    penup()
    setposition(x,y)
    pendown()
    for i in range(5):
        fd(length)
        right(145)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
mainloop()