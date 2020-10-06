#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Àreas Figuras
import math

a = raw_input()
if a == 'quadrado' or a == 'círculo':
	b = float(raw_input())
	if a == 'quadrado':
		area = b ** 2
		print 'Área do quadrado: %.2f (cm2)' % (area)
	elif a == 'círculo':
		area = math.pi * (b ** 2)
		print 'Área do círculo: %.2f (cm2)' % (area)
elif a == 'retângulo' or a == 'triângulo':
	c = float(raw_input())
	d = float(raw_input())
	if a == 'retângulo':
		area = c * d
		print 'Área do retângulo: %.2f (cm2)' % (area)
	if a == 'triângulo':
		area = (c * d) / 2
		print 'Área do triângulo: %.2f (cm2)' % (area)
