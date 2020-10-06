#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Classifica Corredor

km = float(raw_input())
horas = float (raw_input())
velocidade = float(km) / float(horas)

if velocidade < 10:
	print 'Velocidade: %.1fkm/h. Corredor amador.' % (velocidade)
elif 10 <= velocidade <= 15:
	print 'Velocidade: %.1fkm/h. Corredor aspirante.' % (velocidade)
elif velocidade > 15:
	print 'Velocidade: %.1fkm/h. Corredor profissional.' % (velocidade)
