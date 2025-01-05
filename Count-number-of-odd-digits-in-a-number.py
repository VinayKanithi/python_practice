n=int(input())
c=0
while(n!=0):
    s=n%10
    if(n%2!=0):
        c+=1
    n//=10
print(c)