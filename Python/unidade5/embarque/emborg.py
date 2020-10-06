#coding: utf-8	
#Gabriel Dnatas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Embarque Organizado

def meu_split(palavra):
	s = ''
	l = []
	for i in range(len(palavra)):
		if palavra[i] != ' ':
			s += palavra[i]
		elif s != '':
			l.append(int(s))
			s = ''
	if s != '':
		l.append(int(s))
	return l

while True:
	passageiros = raw_input()
	ordem = meu_split(passageiros)
	break

l = []
l2 = []
for i in range(len(ordem)):
	l.append(ordem[i])
	if ordem[i] % 2 == 0:
		continue
	else:
		l2.append(ordem[i])
for i in range(len(ordem)):
	if ordem[i] % 2 == 0:
		l2.append(ordem[i])
	else:
		continue
if l == l2:
	print 'ok'
else:
	print 'erro'
