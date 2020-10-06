#coding: utf-8  
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Aula de Médias

soma_notas = 0.0
quant = 0
l = []

while True:
	nota = float(raw_input())
	soma_notas += nota
	quant += 1
	l.append(nota)
	if soma_notas >= 100:
		break
media = soma_notas / quant
print 'Quantidade de números lidos: %d' % (quant)
print 'Soma dos números lidos: %.2f' % (soma_notas)
print 'Média = %.2f' % (media)
print ''
print 'Abaixo da média'
for i in range(len(l)):
	if l[i] < media:
		print '%.2f (%do)' % (l[i], i + 1)
print ''
print 'Acima da média'
for i in range(len(l)):
	if l[i] > media:
		print '%.2f (%do)' % (l[i], i + 1)
