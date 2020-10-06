#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Descarta coincidente

quant_num = int(raw_input())

aceitos = []
descartados = []
ace = 0
des = 0

for i in range(quant_num):
	num = raw_input()
	controle = True
	for j in range(len(num)):
		if int(num[j]) == j:
			descartados.append(num)
			des += 1
			controle = False
			break
	if controle:
		aceitos.append(num)
		ace += 1
			
print '---'
print '%d aceito(s)' % (ace)
for q in aceitos:
	print q
print '%d descartado(s)' % (des)
for q in descartados:
	print q
