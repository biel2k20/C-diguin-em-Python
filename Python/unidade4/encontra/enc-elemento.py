#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Encontra Elementos
def meu_in(e, seq):
	for i in range(len(seq)):
		if seq[i] == e:
			return True
	return False

num = int(raw_input())
inteiros = raw_input()
l_inteiros = []
for i in range(len(inteiros)):
	if inteiros[i] != ' ':
		l_inteiros.append(int(inteiros[i]))

if meu_in(num, l_inteiros):
	print 'sim'
else:
	print 'não'
