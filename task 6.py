n=int(input())
factorial=1
for i in range(1,n+1):#Здесь мы считаем факториал числа путём умножения числа i на 1, после чего мы прибавим к факториалу 1(это по заданию)
    factorial*=i
s=factorial+1
print(s)
