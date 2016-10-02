# -*- coding : utf-8 -*-
#numbers of large numbers to sum

#Challenge : https://www.hackerrank.com/challenges/a-very-big-sum

n = int(input())

numbers_str = str(input())
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

print(soma)