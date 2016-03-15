# coding: UTF-8
# セット（集合型） - 重複を許さない
a = set([1, 2, 3, 4,5,2,3,4])
b = set([3, 4, 5,7])

print a
print a - b
# | 
print a | b
# & 
print a & b
# ^
print a ^ b