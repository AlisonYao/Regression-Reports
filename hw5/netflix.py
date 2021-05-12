f = open('data2.txt', 'r')
lines = f.readlines()

count = 0
countAll = 0
cancelled, renewed = 0, 0
for line in lines:
    countAll += 1
    line = line.strip('\n')
    if 'Netflix' in line:
        # print(line)
        count += 1
        if 'Renewed' in line:
            renewed += 1
            print(line)
        else:
            cancelled += 1
            # print(line)

f.close()
print(countAll, count, cancelled, renewed)
