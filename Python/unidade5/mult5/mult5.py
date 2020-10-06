#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Múltiplos de 5

limite = int(raw_input())
mults = range(5,limite,5)

l = []
for i in range(len(mults)):
	if mults[i] % 2 == 0:
		l.append(mults[i])
for i in range(len(l)):
	print l[i]
