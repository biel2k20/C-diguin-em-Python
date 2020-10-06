#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Analytics Assembleia

def conta_votos(votacoes, id_votacao):
	def my_split(palavra):
		s = ''
		l = []
		for i in range(len(palavra)):
			if palavra[i] != ',':
				s += palavra[i]
			elif s != '':
				l.append(s)
				s = ''
		if s != '':
			l.append(s)
		return l
	l = []
	cs = 0
	cn = 0
	for i in range(len(votacoes)):
		votos = my_split(votacoes[i])
		if votos[2] == str(id_votacao):
			if  votos[1] == 'sim':
				cs += 1
			elif votos[1] == 'nao':
				cn += 1
	l.append(cs)
	l.append(cn)
	return l
		
		
