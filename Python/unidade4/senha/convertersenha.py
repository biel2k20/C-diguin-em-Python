#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Converte senha

def meu_in(caractere, sequencia):
	for i in sequencia:
		if i == caractere:
			return True
	return False
palavra = raw_input()

s = ''
s += palavra[0]
cont = 0
for e in range(1,len(palavra)):
	if not(meu_in(palavra[e], 'aeioAEIO')):
		s += palavra[e]
		continue
	if meu_in(palavra[e], 'aA'):
		s += '4'
		cont += 1
	elif meu_in(palavra[e], 'eE'):
		s += '3'
		cont += 1
	elif meu_in(palavra[e], 'iI'):
		s += '1'
		cont += 1
	elif meu_in(palavra[e], 'oO'):
		s += '0'
		cont += 1

print s + ' (%d troca(s))' % (cont)
