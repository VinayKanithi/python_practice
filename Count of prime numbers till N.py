n=int(input())
i,j,k,c=0,0,0,0
while(i<=n):
    for j in range(2,i+1):
        if i%j==0:
            c+=1
    if c==1:
        k+=1
    c=0
    i+=1
print(k)