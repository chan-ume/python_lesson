# coding:UTF-8
#リスト

sales = [255,100, 353,400]
print len(sales)
print sales[2]
sales[2]=100
print sales[2]

# in
print 100 in sales #True or false
# range
print range(10)
print range(3,10,2)


sales.sort()
print sales

sales.reverse()
print sales

d ="2016/03/15"
print d.split("/")

a = ["a", "b", "c"]
print "-".join(a)