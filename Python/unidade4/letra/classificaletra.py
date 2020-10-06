#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Classifica Letra

palavra = raw_input()

for i in range(len(palavra)):
	if palavra[i] in 'aeiouAEIOU':
		print '<%s> sim' % (palavra[i])
	else:
		print '<%s> nao' % (palavra[i])
