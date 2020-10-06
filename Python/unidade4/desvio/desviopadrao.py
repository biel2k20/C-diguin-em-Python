#coding: utf-8  
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Desvio Padrão

sequencia1 = raw_input().split()
sequencia2 = raw_input().split()
valores_m1= 0.0
valores_m2 = 0.0
cont1 = 0.0
cont2 = 0.0

for i in range(len(sequencia1)):
    valores_m1 += float(sequencia1[i])
    cont1 += 1.0
for i in range(len(sequencia2)):
	valores_m2 += float(sequencia2[i])
	cont2 += 1.0

media2 = valores_m2 / cont2
media1 = valores_m1 / cont1

cima1 = 0.0
cima2 = 0.0
for i in range(len(sequencia1)):
	cima1 += (float(sequencia1[i]) - float(media1)) ** 2
desvio1 = (float(cima1) / (cont1 - 1)) ** 0.5
for i in range(len(sequencia2)):
	cima2 += (float(sequencia2[i]) - float(media2)) ** 2
desvio2 = (float(cima2) / (cont2 - 1)) ** 0.5

if desvio1 == desvio2:
	print 'As sequências possuem o mesmo desvio padrão (%.2f).' % (desvio1)
elif desvio1 > desvio2:
	print 'A sequência 1 possui o maior desvio padrão (%.2f).' % (desvio1)
else:
	print 'A sequência 2 possui o maior desvio padrão (%.2f).' % (desvio2)
