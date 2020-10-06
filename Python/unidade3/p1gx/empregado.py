#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Custo Empregado

salario = float(raw_input())
dias = float(raw_input())
transporte = float(raw_input())
perc_trans = transporte /
 100.0 * salario
perc_fgts = salario / 100.0 * 8
perc_inss = salario / 100.0 * 12

if salario <= 1317.07:
	alq = salario * 0.08
	inss = salario * 0.12
	fgts = salario * 0.08
	if perc_trans > 6:
		v_pag = salario * 0.06
		percn = perc_trans - 6
		v_em = salario * percn
		nsalario = salario - alq + inss + fgts - v_em + v_pag
		print nsalario
