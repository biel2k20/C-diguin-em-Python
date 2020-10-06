#coding: utf-8

def m_in(ls, seq):
	for i in ls:
		if i == seq:
			return True
	return False
def get_choque_horario(l):
	aux = []
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i][len(l[i])-1] == l[j][len(l[j])-1]:
				if not m_in(aux, l[i]):
					aux.append(l[i])
				if not m_in(aux, l[j]):
					aux.append(l[j])
	return aux
