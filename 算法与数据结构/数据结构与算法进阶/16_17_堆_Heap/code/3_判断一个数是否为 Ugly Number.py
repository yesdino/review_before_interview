'''
判断一个数是否为丑数
丑数：只能被 2,3,5 整除净的数
'''
def uglyNumber(num):
    if num <= 0:
        return False
    
    while num % 2 == 0:
        num = num / 2
    while num % 3 == 0:
        num = num /3
    while num % 5 == 0:
        num = num / 5
     
    return num == 1

# ------------------------------------------------
ret = [x for x in range(15) if uglyNumber(x)]
print(ret)