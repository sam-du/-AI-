"""
定义函数实现：
给定列表 numbers = [1, 3, 6, 5, 2, 9, 7, 8]，
函数返回一个新列表，其中每个偶数平方，奇数保持原值。
"""
from pickle import TRUE


numbers = [1,3,6,5,2,9,7,8]
def even_square (lst):
    result = []
    for items in lst:
        if items % 2 == 0:
            value = items**2
            result.append(value)
        else:
            result.append(items)
    return result

print(even_square(numbers))






"""
定义函数实现: 
对于一个任意的整数, 判断其是否为回文整数(负整数不是回文整数)。
回文整数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如, 121 是回文, 而 123 不是。
"""

def isPalimdrone (num):
    s = str(num)
    if s == s[::-1]:
        return True
    return False  

print(isPalimdrone(123))




"""
定义函数实现: 对于一个任意的正整数, 判断其是否为阿姆斯特朗数。

如果一个n位正整数等于其各位数字的n次方之和, 则称该数为阿姆斯特朗数。 例如1**3 + 5**3 + 3**3 = 153。

1000以内的阿姆斯特朗数:  1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
"""

def isArmstrong (num):
    sum = 0
    s = str(num)
    digits = len(s)
    for i in s:
        sum = sum + int(i)**digits
    if sum == num:
        return True
    return False
print(isArmstrong(154))




