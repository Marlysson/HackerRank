# -*- coding : utf-8 -*-

import unittest
import sys

sys.path.append("../")

from solve_me_first import solveMeFirst

class TestSolveMeFirst(unittest.TestCase):

	def test_levanta_excecao_com_valores_incorretos(self):
		self.assertRaises(ValueError,solveMeFirst,"a","a")
	
	def test_levanta_excecao_com_tipos_diferentes(self):
		self.assertRaises(ValueError,solveMeFirst,"a",2)

	def test_retorno_simples_correto(self):
		retorno = solveMeFirst(5,4)

		self.assertEqual(retorno,9)

	def test_retorno_errado(self):
		retorno = solveMeFirst(1,5)

		self.assertNotEqual(retorno,10)

if __name__ == "__main__":
	unittest.main()