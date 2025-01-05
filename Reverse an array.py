# n=int(input())
# a=list(map(int,input().split()))[:n]
# b=a[::-1]
# print(b)
import string
n=int(input())
a=list(map(int,input().split()))[:n]
b=a
c=a.sort()
if a==c:
    print("True")
else:
    print("False")