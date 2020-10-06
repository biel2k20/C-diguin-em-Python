#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Concurso

c1nota1 = float(raw_input())
c1nota2 = float(raw_input())
c1nota3 = float(raw_input())
c1idade = int(raw_input())

c2nota1 = float(raw_input())
c2nota2 = float(raw_input())
c2nota3 = float(raw_input())
c2idade = int(raw_input())

media1 = (c1nota1 * 0.3) + (c1nota2 * 0.4) + (c1nota3 * 0.3)
media2 = (c2nota1 * 0.3) + (c2nota2 * 0.4) + (c2nota3 * 0.3)

if media1 > media2:
	print 'O primeiro candidato foi aprovado com média %.1f.' % (media1)
elif media2 > media1:
	print 'O segundo candidato foi aprovado com média %.1f.' % (media2)
elif media1 == media2:
	if c1idade > c2idade:
		print 'O primeiro candidato foi aprovado com média %.1f.' % (media1)
	elif c2idade > c1idade:
		print 'O segundo candidato foi aprovado com média %.1f.' % (media2)
	else:
		print 'Empate.'
