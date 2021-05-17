import random

word_bank = [
    ['destroy', '파괴하다'], ['wound', '상처를 입히다'], ['spoil', '망쳐놓다'], ['waste', '낭비하다'], ['suffer', '고통을 겪다'],
    ['interpret', '해석하다'], ['groan', '신음하다'], ['conclude', '결론짓다'], ['prove', '증명하다'], ['inspect', '검사하다']
]
""" word_bank = {
    'destroy':'파괴하다', 'wound':'상처를 입히다', 'spoil':'망쳐놓다', 'waste':'낭비하다', 'suffer':'고통을 겪다',
    'interpret':'해석하다', 'groan', '신음하다'], ['conclude', '결론짓다'], ['prove', '증명하다'], ['inspect', '검사하다']
} """
test = True
count = 0
score = 0

print("========= 영어 단어 시험을 시작합니다. ==========\n")

while test:
    words = random.sample(word_bank, 4)
    answer_index = random.randint(0, 3)
    count += 1
    print(f"문제 {count} : {words[answer_index][0]}의 뜻은?")
    for i in range(len(words)):
        print(f"({i+1}) {words[i][1]}")

    user_input = int(input("정답은 몇 번일까요?(종료하려면 0) >>> "))
    if user_input == 0:
        test = False
        print(f"테스트를 종료합니다. 총 {count-1} 문제 중 {score} 문제를 맞추셨습니다.")
    elif user_input == answer_index + 1:
        score += 1
        print("정답입니다.")
    else:
        print(f"땡! 정답은 {answer_index+1}번입니다.")
    print()
