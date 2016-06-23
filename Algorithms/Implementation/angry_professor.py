# # -*- coding:utf8 -*-

def verificar_aula_cancelada(dados_da_classe,horarios_alunos):
	quant_minima = dados_da_classe[1]
	
	quant_alunos_no_horario = 0

	for horario in horarios_alunos:
		if horario <= 0:
			quant_alunos_no_horario += 1

	if quant_alunos_no_horario >= quant_minima:
		return "NO"
	else:
		return "YES"