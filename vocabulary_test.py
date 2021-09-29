import random

word_bank = [
    ['destroy', '파괴하다'], ['wound', '상처를 입히다'], ['spoil', '망쳐놓다'], ['waste', '낭비하다'], ['suffer', '고통을 겪다'],
    ['interpret', '해석하다'], ['groan', '신음하다'], ['conclude', '결론짓다'], ['prove', '증명하다'], ['inspect', '검사하다'],
    ['increase', '증가하다'], ['respect', '존경하다'], ['object', '반대하다'], ['decrease', '감소하다'], ['advise', '충고하다']
]
test = True
count = 0
score = 0

print("========= 영어 단어 시험을 시작합니다. ==========\n")

while count < 10:
    words = random.sample(word_bank, 4) # 총 문항 10개, 보기가 4개가 나와야 하므로 word_bank의 길이를 14개 이상으로 함.
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
        word_bank.remove(words[answer_index])   # 정답을 맞춘 문제는 다시 출제되지 않도록 리스트에서 삭제
    else:
        print(f"땡! 정답은 {answer_index+1}번입니다.")    
    print(word_bank)
    print()

    if count == 10:
        print(f"모든 문제를 다 풀었습니다. 총 {count} 문제 중 {score} 문제를 맞추셨습니다.")
        break

