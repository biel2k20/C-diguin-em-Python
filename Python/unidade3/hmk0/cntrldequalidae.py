#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Controle de Qualidade

peso_cong = float(raw_input())
peso_dps = float(raw_input())
peso_ag = peso_cong - peso_dps
perc_ag = peso_ag * 100.0 / peso_cong

if perc_ag >= 5 and perc_ag < 10:
	print '%.1f%% do peso do produto é de água congelada.' % (perc_ag)
	print 'Produto em conformidade.'
elif perc_ag >= 10:
	print '%.1f%% do peso do produto é de água congelada.' % (perc_ag)
	print 'Produto não conforme.'
elif perc_ag < 5:
	print '%.1f%% do peso do produto é de água congelada.' % (perc_ag)
	print 'Produto qualis A.'
