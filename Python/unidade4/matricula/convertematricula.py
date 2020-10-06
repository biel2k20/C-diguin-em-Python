#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Converte matrícula

matricula = raw_input()
s = '1'

for i in range(1,len(matricula)):
	if i == 5:
		break
	s += matricula[i]
s += '0'
for i in range(5,len(matricula)):
	s += matricula[i]
	
print s
