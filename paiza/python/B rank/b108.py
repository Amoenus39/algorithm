n, m = list(map(int, input().split(' ')))
gon = []
group = []

for i in range(n):
    a = int(input())
    gon.append(a)
for i in range(m):
    a = int(input())
    group.append(a)

blank = [0 for _ in range(len(gon))]
result = [0 for _ in range(len(gon))]


for i in range(len(group)):
    while group[i] > 0:
        for j in range(len(gon)):
            if blank[j] == 0:
                if group[i] == 0:
                    continue
                if gon[j] >= group[i]:
                    result[j] += group[i]
                    group[i] = 0
                    blank[j] = 1
                else:
                    result[j] += gon[j]
                    group[i] = group[i] - gon[j]
                    blank[j] = 1
            if blank[len(gon)-1] == 1:
                blank = [0 for _ in range(len(gon))]

for el in result:
    print(el)