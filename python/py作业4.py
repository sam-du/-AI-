"""
实现程序：请用户输入一个正整数 n, 程序计算并输出该整数「各位数字之积」与「各位数字之和」的差

示例:
输入: n = 234
输出: 15 

解释:
各位数之积 = 2 * 3 * 4 = 24 
各位数之和 = 2 + 3 + 4 = 9 
结果 = 24 - 9 = 15
"""
integer = int(input("请输入一个正整数:"))
product = 1
sum = 0 
while integer > 0:
    digit = integer % 10
    product = product * digit 
    sum = sum + digit 
    integer = integer // 10
result = product - sum
print(result)





"""
已知字典 d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}, 计算键和值中所有数字类型的数据之和

即: 100 + 8.1 + True + 3+4j = (112.1+4j)
"""
d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}
sum = 0 
for key, value in d.items():
    # isinstace 判断类型 判断key和value是否为数字类型 (int, float) 是则加到sum中 
    if isinstance(key, (int, float, bool, complex)):
        sum = sum + key
    if isinstance(value, (int, float, bool, complex)):
        sum = sum + value
print(sum)



"""
给你一个整数列表lst, 实现程序： 判断列表中是否存在连续三个元素都是奇数的情况: 如果存在，请输出 True; 否则输出 False
示例 1:
输入: lst = [2, 6, 4, 1]
输出: False
解释: 不存在连续三个元素都是奇数的情况

示例 2:
输入: lst = [1, 2, 34, 3, 4, 5, 7, 23, 12]
输出: True
解释: 存在连续三个元素都是奇数的情况，即 [5, 7, 23]
"""
lst = [1, 2, 34, 3, 4, 5, 7, 23, 12]
count = 0
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        count += 1
        if count == 3:
            print(True)
            break
    else:
        count = 0
else:
    print(False)






