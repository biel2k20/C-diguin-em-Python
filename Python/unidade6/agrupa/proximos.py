#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Agrupa próximos

def agrupa_proximos(lista, valor, criterio):
	l = []
	for i in range(len(lista)):
		if abs(lista[i] - valor) < criterio:
			l.append(lista[i])
	return l
l = [1,2,3,4,8,22,3,5]
b = agrupa_proximos(l, 4, 2)
print b
