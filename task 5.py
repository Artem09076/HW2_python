n=int(input())
x=0
s=0
while n!=0: 
    if n>x:
        x=n
        s=1
    elif n==x:
        s+=1
    n=int(input()) 
print(s)
