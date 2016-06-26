# -*- coding : utf-8 -*-

import unittest
import sys

sys.path.append("../")

from a_very_big_sum import to_list , convert , sum_numbers

class TestAveryBigSum(unittest.TestCase):
		
	def setUp(self):
		self.numeros1 = '1000000001 1000000002 1000000003'
		self.numeros2 = '1000000001, 1000000002, 1000000003'
		self.numeros3 = '1000000001,1000000002,a'

	def test_tipo_lista_retornada(self):
		lista = []

		lista.append(to_list(self.numeros1))
		lista.append(to_list(self.numeros2))
		lista.append(to_list(self.numeros3))

		for item in lista:
			self.assertEqual(type(item),list)
			
	def test_retorna_lista_correta_caracteres_aleatorios1(self):
		lista = to_list(self.numeros1)

		self.assertEqual(lista,['1000000001','1000000002','1000000003'])

	def test_retorna_lista_correta_caracteres_aleatorios2(self):
		lista = to_list(self.numeros2)

		self.assertEqual(lista,['1000000001','1000000002','1000000003'])

	def test_retorna_lista_correta_caracteres_aleatorios3(self):
		lista = to_list(self.numeros3)

		self.assertEqual(lista,['1000000001','1000000002','a'])

	def test_excecao_conversao_tipo_incompativel(self):
		self.assertRaises(ValueError,convert,"a")

	def test_excecao_conversao_valores_incompativeis(self):
		lista = to_list(self.numeros3)

		self.assertRaises(ValueError,convert,lista)

	def test_excecao_soma_valores_incompativeis(self):
		lista = to_list(self.numeros3)

		self.assertRaises(TypeError,sum_numbers,lista)

	def test_conversao_valores_compativeis_como_strings(self):
		self.assertEqual(convert(["4","2","3"]),[4,2,3])

	def test_conversao_valores_corretos(self):
		lista = to_list(self.numeros2)
		convertidos = convert(lista)

		self.assertEqual(convertidos,[1000000001,1000000002 ,1000000003])

	def test_soma_correta_valores_corretos(self):
		lista = to_list(self.numeros2)
		convertidos = convert(lista)
		soma = sum_numbers(convertidos)

		self.assertEqual(soma,3000000006)
		
if __name__ == "__main__":
	unittest.main()