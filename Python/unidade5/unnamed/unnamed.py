#coding: utf-8	
#Gabriel Dnatas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Unnamed

conjunto_de_conjuntos = []
conjunto = []
entrada = ""
contador = 0
elementos = 0
while entrada != "fim":
	entrada = raw_input()
	if entrada == "fim":
		break
	elif int(entrada) >= 0:
		conjunto.append(entrada)
	elif int(entrada) < 0:
		conjunto_de_conjuntos.append(conjunto)
		conjunto = []

maior_conjunto = 0
for n in range(len(conjunto_de_conjuntos)):
	if len(conjunto_de_conjuntos[n]) > maior_conjunto:
		maior_conjunto = len(conjunto_de_conjuntos[n])
		contador = n
		elementos = len(conjunto_de_conjuntos[n])
	elif len(conjunto_de_conjuntos) == 1:
		contador = n
		elementos = len(conjunto_de_conjuntos)

if len(conjunto_de_conjuntos) > 0:
	print "Conjunto %d - %d elemento(s)" %(contador + 1, elementos)
