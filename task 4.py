n=int(input())
s=n
max_d=0
while n!=0:
    if n>s:
        max_d+=1
    elif n==s:
        max_d=0
    else:
        max_d=1
print (max_d)
