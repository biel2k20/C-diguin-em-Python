#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Inverte 2 a 2

def inverte2a2_condicional(seq):
	if len(seq) % 2 == 0:
		for i in range(len(seq)-1,0,-1):
			for j in range(len(seq) - 1):
				if seq[j] < seq[j + 1]:
					seq[j], seq[j + 1] = seq[j + 1], seq[j]
	else:
		for i in range(len(seq)-1):
			if seq[i] < seq[i + 1]:
				seq[i], seq[i + 1] = seq[i + 1], seq[i]
	return seq
seq = [3,1,2,3,10,5,6]
print inverte2a2_condicional(seq)
