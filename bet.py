import bet_icon; import bet_quest
import random

print("*" * 100)
print("베팅 게임에 오신 것을 환영합니다.")
print("레벨을 통과하실 때마다 베팅 금액의 두 배를 상금으로 받을 수 있습니다.")
print("하지만 레벨 통과에 실패하면 베팅한 금액을 모두 잃게 됩니다.")
print("*" * 100)

bet = int(input("게임을 시작하려면, 베팅금액을 입력하세요(단위 $). >>>>> "))
print(f"총 ${bet} 를 베팅하셨습니다.")
print()

quests = bet_quest.quests
icons = bet_icon.icons

def betting(a):
    i = 0
    prize = a
    while i < 3:
        answer = random.randint(1, 3)
        print(icons[i])
        print(quests[i])
        choice = int(input("당신의 선택은? 1, 2, 3 >>>>>>  "))
        if answer == choice:
            prize *= 2
            print(f"와우! 축하합니다! 베팅한 금액이 두 배가 되었습니다. 총 금액은 ${prize} 입니다.")
            if i == 2:
                print("모든 도전을 성공하셨습니다. 게임을 종료합니다.")
                break
            print("다음 단계에 도전하시겠습니까? 도전에 성공하면 현재 금액의 두 배를 획득하나, 실패하면 모든 금액을 잃게 됩니다.")
            confirm = input("도전하려면 'y'를, 그만 두려면 'n'을 누르세요. y/n >>>>>  ").lower()
            if confirm == 'y':                
                i += 1
            else: 
                print(f"도전을 종료합니다. 획득한 금액은 ${prize} 입니다.")
                break
        else: 
            print(f"안타깝군요. 정답은 {answer}번이었습니다. 베팅한 금액을 모두 잃었습니다.")
            print(f"다시 도전하려면 F5를 누르세요.")
            break

betting(bet)