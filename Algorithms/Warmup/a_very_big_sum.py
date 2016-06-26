# -*- coding : utf-8 -*-
#numbers of large numbers to sum
n = 5

numbers_str = '1000000001!1000000002  1000000003;1000000004~1000000005'
numbers = []

def to_list(string_numbers):
	from string import punctuation

	for caractere in punctuation:
		string_numbers = string_numbers.replace(caractere," ")

	return string_numbers.strip().split()

def convert(lista):
	return map(int,lista)

def sum_numbers(numbers):
	return sum(numbers)

numbers = to_list(numbers_str)
converted = convert(numbers)
soma    = sum_numbers(converted)

# print(soma)