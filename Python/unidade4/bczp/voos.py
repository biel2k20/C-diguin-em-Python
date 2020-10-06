#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Autorização voos

minutos_decolagem = float(raw_input())
avioes = int(raw_input())
tempos = []
for e in range(avioes):
	tempo_decolar = float(raw_input())
	tempos.append(tempo_decolar)
cont = 0
for t in range(len(tempos)):
	if tempos[t] <= minutos_decolagem:
		disponivel = minutos_decolagem - tempos[t]
		cont += 1 
		minutos_decolagem = disponivel

print '%d voo(s) autorizados.' % (cont)
