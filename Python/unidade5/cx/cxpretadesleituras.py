#coding: utf-8   
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Caixa Preta (descartando leituras)


controle = True
contp = 0
contc = 0
conta = 0
while True:
	dados = raw_input().split()
	peso = int(dados[0])
	combust = int(dados[1])
	altitude = int(dados[2])
	for i in range(len(dados)):
		if peso >= 0 and int(dados[i]) == peso:
			contp += 1
		elif combust >= 0 and int(dados[i]) == combust:
			contc += 1
		elif altitude >= 0 and int(dados[i]) == altitude:
			conta += 1
		else:
			break
	if controle:
		if int(dados[0]) < 0:
			print 'dado inconsistente. peso negativo.'
			controle = False
			break
		elif int(dados[1]) < 0:
			print 'dado inconsistente. combustível negativo.'
			controle = False
			break
		elif int(dados[2]) < 0:
			print 'dado inconsistente. altitude negativa.'
			controle = False
			break

print 'peso: %d' % (contp)
print 'combustível: %d' % (contc)
print 'altitude: %d' % (conta)
