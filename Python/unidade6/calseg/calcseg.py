#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Cálculo de Seguro

def calcula_seguro(valor, lista):
	l = []
	pts = 0
	if int(lista[0]) <= 21 or lista[0] > 60:
		pts += 20
	elif 22 <= int(lista[0]) <= 30:
		pts += 15
	elif 31 <= int(lista[0]) <= 40:
		pts += 12
	elif 41 <= int(lista[0]) <= 60:
		pts += 10
	if lista[1] == True:
		pts += 10
	else:
		pts += 20
	if lista[2] == True:
		pts += 20
	else:
		pts += 10
	if lista[3] == True:
		pts += 20
	else:
		pts += 10
	if lista[4] == True:
		pts += 20
	else:
		pts += 10
	if lista[5] == True:
		pts += 10
	else:
		pts += 20
	if lista[6] == 'Trabalho':
		pts += 10
	else:
		pts += 20
	l.append(pts)
	if pts <= 80:
		l.append('Risco Baixo')
		pagar = valor * 0.10
	elif 80 < pts <= 100:
		l.append('Risco Medio')
		pagar = valor * 0.20
	else:
		l.append('Risco Alto')
		pagar = valor * 0.30
	l.append(pagar)
	return l
