# -*- coding : utf8 -*-

string_entrada = "-4 3 -9 0 4 1"
dados = {"positivos":0 , "negativos":0, "neutros":0}

numeros_teste = map(int,string_entrada.strip().split(" "))

for numero in numeros_teste:
	if numero > 0:
		dados["positivos"] += 1
	elif numero < 0:
		dados["negativos"] += 1
	elif numero == 0:
		dados["neutros"] += 1

def calculos(dados):
	chaves = dados.keys()

	for chave in chaves:
		dados[chave] = "{:.6f}".format( float(dados[chave]) / float(len(numeros_teste)) )

	return dados

dados = calculos(dados)

print(dados["positivos"])
print(dados["negativos"])
print(dados["neutros"])