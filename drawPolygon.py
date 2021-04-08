import turtle

turtle.shape("turtle")
p = int(turtle.numinput("polygon", "num?"))
colors = ["black", "blue", "red", "green"]
while p > 0:
    turtle.color(colors[p % len(colors)])
    for i in range(p):
        turtle.forward(100)
        turtle.left(360/p)
    p -= 1

