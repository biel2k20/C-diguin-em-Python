#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Op Bancárias

def meu_split(palavra):
	s = ''
	l = []
	for i in range(len(palavra)):
		if palavra[i] != ' ':
			s += palavra[i]
		elif s != '':
			l.append(s)
			s = ''
	if s != '':
		l.append(s)
	return l
			
entrada = meu_split(raw_input())
i = 0
valor = float(entrada[1])
while True:
	op = meu_split(raw_input())
	if op[0] == '3':
		break
	if op[0] == '1':
		valor -= float(op[1])
	if op[0] == '2':
		valor += float(op[1])
print 'Saldo de R$ %.2f na conta de %s' % (valor, entrada[0])
		
