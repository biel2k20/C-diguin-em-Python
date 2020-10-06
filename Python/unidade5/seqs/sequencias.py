#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Imprime sequência

def meu_split(palavra):
	s = ''
	l =[]
	for i in range(len(palavra)):
		if palavra[i] != ' ':
			s += palavra[i]
		elif s != '':
			l.append(int(s))
			s = ''
	if s != '':
		l.append(int(s))
	return l

alvo = int(raw_input())
l = []
l1 = []
cont = 0
conts = []
while True:
	sequencia = raw_input()
	if sequencia == 'fim':
		break
	else:
		int_sequencia = meu_split(sequencia)
		l.append(sequencia)
		l1.append(int_sequencia)
	for e in int_sequencia:
		if e > alvo:
			cont += 1
	conts.append(cont)
	cont = 0
for i in range(len(conts)):
	if conts[i] > len(l1[i]) / 2 :
		print 'sequencia %d: %s' % (i + 1, l[i])
