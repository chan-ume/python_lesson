# coding: UTF-8
# リスト <>関数　map

def double(x):
    return x*x
    
print map(double,[2,5,8])

# 無名関数
print map(lambda x:x*x,[2,5,8])