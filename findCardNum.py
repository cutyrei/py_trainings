import random

count = 0
print("Do you want to start?")
number = random.randint(1, 100)

while count < 5:    
    user_num = int(input("1-100: "))
    count += 1
    if user_num < number:
        print("up!!", "rest-%d" % (5-count))
    elif user_num > number:
        print("down!!", "rest-%d" % (5-count))
    else:
        break

if user_num == number:
    print("You are great!!", "tried: %d" % count)
else:
    print("Sorry. My numbers was %d" % number)
print("If you want to try again, press F5")