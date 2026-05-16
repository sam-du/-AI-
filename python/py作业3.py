
""" 
请用户输入身高(m)和体重(kg), 并根据BMI公式(体重/身高的平方)计算出的BMI指数来判断用户的体重情况
判断标准：
BMI >= 35 为重度肥胖
30 <= BMI < 35 为中度肥胖
27 <= BMI < 30 为轻度肥胖
23 <= BMI < 27 为超重
18.5 <= BMI < 23 为正常体重
BMI < 18.5 为轻体重
"""
""" 
请用户输入三个不同的整数, 输入时用空格隔开, 利用条件语句判断出这三个整数中的最大值
"""

height = float(input("请输入身高(m):"))
weight = float(input("请输入体重(kg):"))
bmi = weight / height ** 2
if bmi >= 35:
    print("重度肥胖")
elif bmi >= 30:
    print("中度肥胖")
elif bmi >= 27:
    print("轻度肥胖")
elif bmi >= 23:
    print("超重")
elif bmi >= 18.5:
    print("正常体重")
else:
    print("轻体重")









