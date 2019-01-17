def draw_star(x,y,length):
    penup()
    setposition(x,y)
    for i in range(5):
        fd(length)
        right(150)
draw_star()