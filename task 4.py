# n=int(input())
# s=n
# max_d=0
# while n!=0:
#     if n>s:
#         max_d+=1
#     elif n==s:
#         max_d=0
#     else:
#         max_d=1
# print (max_d)

num = int(input())
prev_num = num
incr_len = 0 # Длина текущего монотонного фрагмента, начинающегося с первого элемента
max_incr_len = 0 # Длина наибольшего монотонного фрагмента, начинающегося с первого элемента
decr_len = 0 # Длина текущего монотонного фрагмента, начинающегося с первого элемента
max_decr_len = 0 # Длина наибольшего монотонного фрагмента, начинающегося с первого элемента

num = int(input())
while num != 0:
    if num > prev_num:
        incr_len += 1
        max_incr_len = max(max_incr_len, incr_len)
        decr_len = 1
    elif num < prev_num:
        decr_len += 1
        max_decr_len = max(max_decr_len, decr_len)
        incr_len = 1
    else:
        incr_len += 1
        decr_len += 1

    prev_num = num
    num = int(input())

max_len = max(max_incr_len, max_decr_len)
print(max_len)
