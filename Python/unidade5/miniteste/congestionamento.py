e = raw_input()

i = 0
cont = 0
l = []
while i < len(e):
	if e[i] == 'v':
		cont += 1
	else:
		l.append(cont)
		cont = 0
	l.append(cont)
	i += 1
maior = 0
for x in range(len(l)):
	if l[x] > maior:
		maior = l[x]
print maior
