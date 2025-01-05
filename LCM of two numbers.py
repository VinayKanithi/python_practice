import math
s,g=0,0
a,b=map(int,input().split())
g=math.gcd(a,b)
s=(a*b)/g
print(int(s))