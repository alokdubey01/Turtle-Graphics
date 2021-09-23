import turtle

window = turtle.Screen()
window.bgcolor("white")
colors = ["red", "green", "blue", "yellow", "orange", "violet"]
mpen = turtle.Turtle()
mpen.distance(0, 0)

for x in range(100):
    mpen.pencolor(colors[x % 6])
    mpen.shape("turtle")
    mpen.speed(1000)
    mpen.forward(10)
    mpen.left(5)


# for x in range(200):
#  mpen.pencolor(colors[x % 6])
#  mpen.speed(1000)
#  mpen.left(5)
#  mpen.circle(200)
turtle.done()