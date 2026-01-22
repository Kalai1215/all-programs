import turtle
colors=['yellow','green','red','white','cyan','blue']
t=turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('Black')
t.speed(30)

for i in range(30):
    t.color(colors[i%6])
    t.fd(i*5)
    t.left(26)
    t.width(28)
