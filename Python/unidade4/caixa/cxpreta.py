#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Caixa Preta

quant_medicoes = int(raw_input())

l = []
controle = True
for e in range(quant_medicoes):
	dados = raw_input().split()
	peso = dados[0]
	combust = dados[1]
	altitude = dados[2]
	l.append(peso)
	l.append(combust)
	l.append(altitude)
	if controle:
		if int(dados[0]) < 0:
			print 'dado inconsistente. peso negativo.'
			controle = False
		elif int(dados[1]) < 0:
			print 'dado inconsistente. combustível negativo.'
			controle = False
		elif int(dados[2]) < 0:
			print 'dado inconsistente. altitude negativa.'
			controle = False

cont = 0
for s in range(len(l)):
	if int(l[s]) >= 0:
		cont += 1
	else:
		break
if cont > 0 and cont != 1:	
	print '%d dados válidos.' % (cont)
elif cont == 1:
	print '%d dado válido.' % (cont)
elif cont == 0:
	print '0 dados válidos'
