#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Caixa Registradora

def caixa_registradora(lista, meta):
	l = []
	comissoes = 0.0
	vendas = 0.0
	for i in range(len(lista)):
		vendas += lista[i]
		if lista[i] < 1000:
			comissoes += (lista[i] * 0.05)
		elif 1000 <= lista[i] < 5000:
			comissoes += (lista[i] * 0.10)
		else:
			comissoes += (lista[i] * 0.15)
	l.append(vendas)
	l.append(comissoes)
	if (vendas - comissoes) >= meta:
		l.append('Lucro')
	else:
		l.append('Prejuizo')
	return l
