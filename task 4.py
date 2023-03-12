
num = int(input())
prev_num = num
incr_len = 0 
max_incr_len = 0 
decr_len = 0 
max_decr_len = 0 

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
