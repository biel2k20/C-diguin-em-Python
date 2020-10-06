#coding: utf-8	
#Gabriel Dnatas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Fundo de Investimento

cima = 0.0
cont = 0
media = 0
while True:
	valor = float(raw_input())
	if valor >= media:
		cima += valor
		cont += 1
		media = cima / cont
	else:
		break
print 'Saldo total do FIS: R$%.2f.' % (cima)
print 'Média das contribuições: R$%.2f.' % (media)
