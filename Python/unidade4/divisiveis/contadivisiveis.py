#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Conta Divisíveis

valor_K = int(raw_input())
valor_N = int(raw_input())

l = []
cont = 0

for i in range(valor_N):
	inteiro = int(raw_input())
	l.append(inteiro)
for i in range(len(l)):
	if l[i] % valor_K == 0:
		cont += 1
porcentagem = 100.0 / valor_N * cont

print '%d (%.1f%%)' % (cont, porcentagem)
