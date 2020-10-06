#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Karel, o Robô
def meus(p):
	s = ''
	l = []
	for i in range(len(p)):
		if p[i] != ' ':
			s += p[i]
		elif s != '':
			l.append(s)
			s = ''
	if s != '':
		l.append(s)
	return l
x = 0
y = 0
while True:
	entrada = raw_input()
	b = meus(entrada)
	if int(b[1]) == 0:
		print 'Fim de jogo'
		break
	else:
		if entrada[0] == 'C':
			y += int(b[1])
		if entrada[0] == 'D':
			x += int(b[1])
		if entrada[0] == 'B':
			y -= int(b[1])
		if entrada[0] == 'E':
			x -= int(b[1])
	if abs(x) == (2 * abs(y)) or abs(y) == (2 * abs(x)):
		print 'Parabéns, conquista do portal (%d, %d)' % (x , y)
		break
