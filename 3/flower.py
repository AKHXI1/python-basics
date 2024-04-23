import turtle
t=turtle.Turtle()
t.speed(0)
def flower():
    for i in range(5):
        t.circle(180,90)
        t.left(90)
        t.circle(180,90)
        t.left(20)
flower()
turtle.done()