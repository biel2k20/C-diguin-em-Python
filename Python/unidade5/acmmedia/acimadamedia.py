#coding: utf-8  
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Acima da média

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

media_mensal = float(raw_input())

medias = []
while True:
	cima = 0.0
	cont = 0
	num = raw_input()
	lista_num = meu_split(num)
	if lista_num[0] == 'fim':
		break
	for i in range(len(lista_num)):
		cima += int(lista_num[i])
		cont += 1
	media = cima / cont
	if media > media_mensal:
		print num
	if media < media_mensal / 2:
		break
