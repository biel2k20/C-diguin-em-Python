#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Ciclo Trigonométrico

angulo = float(raw_input())

if 0 < angulo < 90:
	print 'Quadrante 1'
elif 90 < angulo < 180:
	print 'Quadrante 2'
elif 180 < angulo < 270:
	print 'Quadrante 3'
elif 270 < angulo < 360:
	print 'Quadrante 4'
elif angulo > 360:
	qua = angulo % 360
	if 0 < qua < 90:
		print 'Quadrante 1'
	elif 90 < qua < 180:
		print 'Quadrante 2'
	elif 180 < qua < 270:
		print 'Quadrante 3'
	elif 270 < qua < 360:
		print 'Quadrante 4'
	elif qua == 0 or qua == 90 or qua == 180 or qua == 270 or qua == 360:
		print 'Sobre eixos'
elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
	print 'Sobre eixos'
