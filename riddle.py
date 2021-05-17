import turtle as t
import time

t.bgcolor("pink")
t.ht()
t.up()
riddles = [
    ['세상에서 가장 비싼 새는?', '백조'],
    ['아홉 명의 자식을 세 글자로 줄이면?', '아이구'],
    ['도둑이 가장 싫어하는 아이스크림은?', '누가바'],
    ['세상에서 가장 추운 바다는?', '썰렁해'],
    ['병든 자여 내게로 오라는 말은 누가 했나?', '엿장수']
]

t.write("수수께끼", False, "center", ("", 50, "bold"))
time.sleep(3)
t.clear()

count = 0
for x, y in riddles:
    t.write(x, False, "center", ("", 30, "bold"))
    user_answer = t.textinput("", "정답을 입력하세요")    
    t.clear()
    if user_answer == y:
        count += 1
        t.write("정답입니다.", False, "center", ("", 50, "bold"))
    else:
        t.write("틀렸습니다.\n 정답은 '%s' 입니다." % y, False, "center", ("", 30, "bold"))
    time.sleep(2)
    t.clear()
    print("\n")

t.write("총 %d 문제를 맞추셨습니다." % count, False, "center", ("", 40, "bold"))
time.sleep(2)