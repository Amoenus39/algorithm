import math

x, y = map(float, input().split())
sum_chr = 0
for i in range(int(x)):
    sum_chr += float(input())

print(math.ceil(round(sum_chr/y, 3)))