#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: No Limite

l = []
while True:
	entrada = raw_input()
	if entrada != '-':
		l.append(float(entrada))
	else:
		break
num = float(raw_input())
cima = 0
media = 0
achou = False

for i in range(len(l)):
	if achou == False:
		cima += l[i]
		media = cima / (i + 1)
		if media > num:
			print 'media = %.1f' % (media)
			print 'num = %d' % (i + 1)
			achou = True

if achou == False:
	print 'limite não alcançado'
