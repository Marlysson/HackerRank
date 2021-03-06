# -*- coding:utf-8 -*-

#Challenge : https://www.hackerrank.com/challenges/simple-array-sum

#Soma normal,incrementando
def soma1(nums):
	soma = 0
	for i in nums.split(' '):
		soma += int(i)
	return soma

#Usando programação funcional
def soma2(nums):
	#transforma a lista de str em int
	nums = [int(i) for i in nums.split(' ')]
	#cria uma função para somar numeros do parametro
	soma = lambda x,y : x+y
	#usa reduce passando a função de soma e os valores a serem somados
	return reduce(soma,nums)

#Usando list comprehension
def soma3(nums):
	return sum([int(i) for i in nums.split(' ')])

n = str(input())
nums = str(input())

print (soma1(nums))
# print (soma2(nums))
# print (soma3(nums))