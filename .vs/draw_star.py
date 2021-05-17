import turtle as t
import random

t.bgcolor("black")
colors = ["yellow", "skyblue", "pink", "green", "white", "red", "orange"]

for x in range(20):
    size = random.randint(10, 50)
    t.speed("fast") # fastest / fast / normal / slow / slowest
    t.up()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.down()
    t.color(random.choice(colors))
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()

t.done() # 그래픽 창 유지