# -*- coding : utf8 -*-
import unittest
from angry_professor import verificar_aula_cancelada

class TestAngryProfessor(unittest.TestCase):

	def test_quant_minima_1(self):
		dados_da_classe = [ 4 , 3 ]
		self.assertEqual(3,dados_da_classe[1])

	def test_quant_minima_2(self):
		dados_da_classe = [ 4 , 2 ]
		self.assertEqual(2,dados_da_classe[1])

	def test_aula_cancelada(self):
		dados_da_classe = [ 4 , 3 ]
		horarios_alunos = [-1 , -3 , 4 , 2]

		cancelada = verificar_aula_cancelada(dados_da_classe,horarios_alunos)

		self.assertEqual("YES",cancelada)

	def test_aula_nao_cancelada(self):
		dados_da_classe = [ 4 , 2]
		horarios_alunos = [0 , -1 , 2 , 1]

		calcelada = verificar_aula_cancelada(dados_da_classe,horarios_alunos)

		self.assertEqual("NO",calcelada)

if __name__ == "__main__":
	unittest.main()