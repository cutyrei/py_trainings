import turtle as t
import time, random

t.bgcolor("pink")
t.ht()
t.up()
t.write("READY", False, "center", ("", 50, "bold")) # turtle.write(arg, move=False, align="center", font=("Arial", 8, "normal"))
time.sleep(3)
t.clear()

numbers = ''
for i in range(3):
    rand_num = random.randint(1, 50)
    t.write(rand_num, False, "center", ("", 100, "bold"))
    numbers += str(rand_num)+" "
    time.sleep(1)
    t.clear()

user_input = t.textinput("숫자기억게임", "숫자를 입력하세요")

if user_input == numbers.strip():
    t.write("정답입니다.", False, "center", ("", 100, "bold"))
else:
    t.write("틀렸습니다.", False, "center", ("", 50, "bold"))
    t.goto(0, -150)
    t.write("정답은 %s 입니다." % numbers, False, "center", ("", 50, "bold"))
