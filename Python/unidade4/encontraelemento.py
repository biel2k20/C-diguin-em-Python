#coding: utf-8

a = int(raw_input())
b = raw_input()
l = []
for i in range(len(b)):
	if b[i] != ' ':
		l.append(int(b[i]))

if a in l:
	print 'sim'
else:
	print 'não'
