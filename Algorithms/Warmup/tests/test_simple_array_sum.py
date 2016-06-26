# -*- coding : utf-8 -*-

import unittest
import sys

sys.path.append("../")

from simple_array_sum import soma1,soma2,soma3

class TestSimpleArraySumSoma1(unittest.TestCase):
	
	def test_separadores_errados_na_funcao(self):
		self.assertRaises(ValueError,soma1,"1,2,3")
	
	def test_mais_tipos_errados_na_funcao(self):
		self.assertRaises(ValueError,soma1,"1 a 3")

	def test_retorno_parametro_correto(self):
		self.assertEqual(soma1("1 2 3 4"),10)

	def test_retorno_errado_parametros_corretos(self):
		self.assertNotEqual(soma1("1 2 3 4 5"),20)


class TestSimpleArraySumSoma2(unittest.TestCase):
	
	def test_separadores_errados_na_funcao(self):
		self.assertRaises(ValueError,soma2,"1,2,3")
	
	def test_mais_tipos_errados_na_funcao(self):
		self.assertRaises(ValueError,soma2,"1 a 3")

	def test_retorno_parametro_correto(self):
		self.assertEqual(soma2("1 2 3 4"),10)

	def test_retorno_errado_parametros_corretos(self):
		self.assertNotEqual(soma2("1 2 3 4 5"),20)


class TestSimpleArraySumSoma3(unittest.TestCase):
	
	def test_separadores_errados_na_funcao(self):
		self.assertRaises(ValueError,soma3,"1,2,3")
	
	def test_mais_tipos_errados_na_funcao(self):
		self.assertRaises(ValueError,soma3,"1 a 3")

	def test_retorno_parametro_correto(self):
		self.assertEqual(soma3("1 2 3 4"),10)

	def test_retorno_errado_parametros_corretos(self):
		self.assertNotEqual(soma3("1 2 3 4 5"),20)

if __name__ == "__main__":
	unittest.main()