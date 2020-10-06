#coding: utf-8   
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Calculadora

def meu_split(palavra):
	s = ''
	l = []
	for i in range(len(palavra)):
		if palavra[i] != ' ':
			s += palavra[i]
		elif s != '':
			l.append(s)
			s = ''
	if s != '':
		l.append(s)
	return l

while True:
	entrada = raw_input()
	valores = meu_split(entrada)
	if int(valores[0]) == 1:
		soma = int(valores[1]) + int(valores[2])
		print soma
	if int(valores[0]) == 2:
		sub = int(valores[1]) - int(valores[2])
		print sub
	if int(valores[0]) == 3:
		mult = int(valores[1]) * int(valores[2])
		print mult
	if int(valores[0]) == 4:
		if int(valores[2]) == 0:
			print 'Erro: Divisão por 0'
			break
		else:
			div = int(valores[1]) / int(valores[2])
			print div
	if int(valores[0]) == 5:
		break
