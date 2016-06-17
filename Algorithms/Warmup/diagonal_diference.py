# -*- coding: utf-8 -*-

arquivo = open("matriz_diagonal_diference.txt")
matriz = []

for linha in arquivo:
	vetor = linha.strip().split(" ")
	matriz.append( map(int,vetor) )

    # Percorrer da esquerda para a direita , somando os índices

def get_princ(matriz):
    indice_vetor = 0
    sum_princ = 0

    # Percorrer da esquerda para a direita , somando os índices
    # INICIO -> FINAL
    for vetor in matriz:
        sum_princ += vetor[indice_vetor]
        indice_vetor += 1
        
    return sum_princ


def get_sec(matriz):
    indice_vetor = len(matriz[0]) - 1 # lenght of a vector
    sum_sec = 0
    
    # Percorrer da direita para a esquerda , substraindo os indices , até chegar no inicio.
    # FINAL -> INICIO
    for vetor in matriz:
        sum_sec += vetor[indice_vetor]
        indice_vetor -= 1
        
    return sum_sec

print("Soma diagonal principal:  {}".format(get_princ(matriz)))
print("Soma diagonal Secundária: {}".format(get_sec(matriz)))

resultado = abs( get_princ(matriz) - get_sec(matriz))

print ("Diferença absoluta: {}".format(resultado))

