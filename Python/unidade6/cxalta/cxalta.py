#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Caixa Alta

def caixa_alta(frase):
	s = ''
	flag = True
	if len(frase) > 1:
		if ord(frase[0]) >= 97 and frase[1] != ' ':
			s += chr(ord(frase[0]) - 32)
		elif ord(frase[0]) >= 97 and frase[1] == ' ':
			s += frase[0]
		elif ord(frase[0]) < 97 and frase[1] == ' ':
			s += chr(ord(frase[0]) + 32)
		elif ord(frase[0]) < 97 and frase[1] != ' ':
			s += frase[0]
		for i in range(1,len(frase)-1):
			viz = frase[i + 1]
			ant = frase[i - 1]
			if ant != ' ' and viz != ' ':
				s += frase[i]
			elif viz != ' ' and ant == ' ':
				if ord(frase[i]) < 97:
					s += frase[i]
				else:
					t = ord(frase[i]) - 32
					m = chr(t)
					s += m
			elif viz == ' ' and ant == ' ':
				if ord(frase[i]) >= 97:
					s += frase[i]
				else:
					f = ord(frase[i]) + 32
					g = chr(f)
					s += g
			elif viz == ' ' and ant != ' ':
				s += frase[i]
		for i in range(len(frase)- 1,-1 ,-1):
			if ord(frase[i]) < 97 and frase[i - 1] == ' ':
				s += chr(ord(frase[i]) + 32)
			else:
				s += frase[i]
			break
	else:
		if ord(frase[0]) >= 97:
			s += frase[0]
		else:
			s += chr(ord(frase[0]) + 32)
	return s

