# -*- coding: utf-8 -*-

arquivo = open("matriz_diagonal_diference.txt")
matriz = []

for linha in arquivo:
	vetor = linha.strip().split(" ")
	matriz.append( map(int,vetor) )

def get_princ(matriz):

	cont = 0
	sum_princ = 0

	for vetor in matriz:
		sum_princ += vetor[cont]
		cont += 1

	return sum_princ


def get_sec(matriz):
	pos = len(matriz) - 1
	index_vetor = 0
	sum_sec = 0

	while index_vetor < len(matriz):
		sum_sec += matriz[index_vetor][pos]
	
		pos -= 1
		index_vetor += 1

	return sum_sec

print("Soma diagonal principal:  {}".format(get_princ(matriz)))
print("Soma diagonal Secundária: {}".format(get_sec(matriz)))

resultado = abs( get_princ(matriz) - get_sec(matriz))

print ("Diferença absoluta: {}".format(resultado))
