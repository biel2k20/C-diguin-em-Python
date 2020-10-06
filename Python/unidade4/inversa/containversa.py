#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Conta Inversa

palavra = raw_input()
cont = 0
inversa = ''
for i in range(len(palavra)-1,-1,-1):
	inversa += palavra[i]
for j in range(len(inversa)):
	if inversa[j] == palavra[j]:
		cont += 1

print 'A palavra %s contém %d caractere(s) coincidente(s) com a sua inversa.' % (palavra, cont)
