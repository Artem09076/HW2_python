n=int(input())
s=0
for a in range(n):
    a=float(input())
    if a==0:
        s+=1
if s>0:
    print("YES")
else:
    print("NO")    

