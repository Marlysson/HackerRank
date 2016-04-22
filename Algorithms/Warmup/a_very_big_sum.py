# -*- coding : utf-8 -*-
#numbers of large numbers to sum
n = 5

numbers_str = '1000000001 1000000002 1000000003 1000000004 1000000005'
numbers = []

for i in numbers_str.split(' '):
	numbers.append(int(i))

print (sum(numbers))