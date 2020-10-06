#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Ciência sem Fronteiras

enem = float(raw_input())
creditos = float(raw_input())
percent_creditos = creditos * 100.0 / 416

if 20 <= percent_creditos <= 90 and enem >= 600:
	print 'Todas as condições satisfeitas.'
elif 20 <= percent_creditos <= 90 and not(enem >= 600):
	print 'Condição ENEM não satisfeita.'
elif not(20 <= percent_creditos <= 90) and enem >= 600:
	print 'Condição CRÉDITOS não satisfeita.'
else:
	print 'Nenhuma condição satisfeita.'
