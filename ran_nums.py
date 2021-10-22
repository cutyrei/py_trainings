import random, csv

result = []
f = open('ran_nums_records.csv', 'r', encoding='utf-8')
records = csv.reader(f)

def check(data):
    data.sort()
    new = []
    for d in data:
        new.append(str(d))
    if new not in records:
        return True
    else:
        print("found", data, new)
        return False
count = 0
while True:
    count += 1
    nums = list(range(1, 46))
    # game = random.sample(nums, 6)
    game = []
    for i in range(6):
        n = random.choice(nums)
        game.append(n)
        nums.remove(n)    
    if check(game): result.append(game)
    if len(result) == 6: break

print(result)


