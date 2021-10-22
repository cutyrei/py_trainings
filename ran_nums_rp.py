import csv

f = open('ran_nums_records.csv', 'r', encoding='utf-8')
records = list(csv.reader(f))

repeated = [0 for n in range(7)]
for i in range(len(records)-1):
    res = []
    for j in records[i]:
        if j in records[i+1]:
            res.append(j)
    print(res, len(res))
    repeated[len(res)] += 1

print("repeated", repeated)

