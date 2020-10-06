#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Analytics Assembleia

def conta_votos(votacoes, id_votacao):
	l = []
	c = 0
	c2 = 0
	for i in range(len(votacoes)):
		if str(id_votacao) in votacoes[i]:
			if 'sim' in votacoes[i]:
				c += 1
			elif 'nao' in votacoes[i]:
				c2 += 1
	l.append(c)
	l.append(c2)
	return l
