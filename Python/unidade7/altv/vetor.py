#coding:utf-8

def altera_vetor_por_escalar(v, n):
	l = []
	for i in range(len(v)-1,-1,-1):
		a = v.pop(i)
		b = a * n
		l.append(b)
	for i in range(len(l)-1,-1,-1):
		v.append(l[i])


