#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Ano bissexto

a = int(raw_input())

if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
	print "%d é bissexto" % (a)
else:
	print "%d não é bissexto" % (a)
