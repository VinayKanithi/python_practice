=int(input())
i,s=0,1
while(i<=n):
    if i==0:
        i=1
    s*=i
    i+=1
print(s)