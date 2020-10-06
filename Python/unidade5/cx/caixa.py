#coding: utf-8   
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Caixa Preta (descartando leituras)


contp = 0
contc = 0
conta = 0
while True:
	dados = raw_input().split()
	peso = int(dados[0])
	combust = int(dados[1])
	altitude = int(dados[2])
	if peso < 0:
		print 'dado inconsistente. peso negativo.'
		break
	contp += 1
	if combust < 0:
		print 'dado inconsistente. combustível negativo.'
		break
	contc += 1 
	if altitude < 0:
		print 'dado inconsistente. altitude negativa.'
		break
	conta += 1
print 'peso: %d' % (contp)
print 'combustível: %d' % (contc)
print 'altitude: %d' % (conta)
