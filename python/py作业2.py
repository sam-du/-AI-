# 已知 lst1 = [3, 1, 2], lst2 = [4, 5, 6], 程序实现: 把lst2中的元素添加到lst1中, 并对lst1进行降序排序
lst1 = [3, 1, 2]
lst2 = [4, 5, 6]
lst1.extend(lst2)
lst1.sort(reverse=True)
print(lst1)


# 已知 lst1 = [1, 2], lst2 = [3, 4], lst3 = [5, 6], 程序实现: 把lst1, lst2作为元素添加到lst3中, 并求lst3的长度
lst1 = [1, 2]
lst2 = [3, 4]
lst3 = [5, 6]
lst3.extend(lst1)
lst3.extend(lst2)
print(len(lst3))

# 已知 lst = [1, 3, 2, 6, 4], 程序实现: 删除lst元素中的最大值和最小值（不考虑多个最值情况）
lst = [1, 3, 2, 6, 4]
max_value = max(lst)
min_value = min(lst)
lst.remove(max_value)
lst.remove(min_value)
print(lst)


# 已知 lst = [1, 3, 2, 6, 4], 程序实现: 删除lst元素中的中位数（只考虑列表中元素个数为奇数的情况）
lst = [1, 3, 2, 6, 4]
median = lst[sorted(lst)[len(lst)//2]]
lst.remove(median)
print(lst)


# 已知 lst = [1, 3, 2, 6, 1, 1, 41], 程序实现: 求lst中最后一个为1的元素的索引
lst = [1, 3, 2, 6, 1, 1, 41]
# 从后往前查找第一个为1的元素的索引
last_1_index = lst.index(1, -1)
print(last_1_index)



