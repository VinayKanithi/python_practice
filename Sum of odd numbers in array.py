n = int(input())
a = list(map(int, input().split()))[:n]
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
s = sum(b)
print(s)
