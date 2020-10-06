#coding: utf-8  
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Abaixo da média

n = ''

l = []
while n != 'fim':
	n = raw_input()
	l.append(n)
cima1 = 0
cont = 0
for i in range(len(l)-1):
	cima1 += int(l[i])
	cont += 1
media = float(cima1) / cont
print '%.2f' % (media)

for i in range(0,len(l)-1):
	if int(l[i]) < media:
		print '%d %d' % (i + 1, int(l[i]))
