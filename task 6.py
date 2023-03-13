n=int(input())
factorial=1
s=1
for i in range(1,n+1):
    factorial/=i#Это штука помогает в нахождении факториала
    s+=factorial#А эта штука прибовлят к факториалу 1(по условию)
print(s)
