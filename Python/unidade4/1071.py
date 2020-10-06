#coding: utf-8

a = int(raw_input())
b = int(raw_input())
soma = 0
if a > b:
	x = (range((a-1),b,-1))
	for e in x:
		if e % 2 != 0:
			soma = soma + e
			soma
	print soma
elif b > a:
	y = (range((a-1),(b+1),1))
	for e in y:
		if e % 2 != 0 and e != 0:
			soma = soma + e
			soma
	print soma
else:
	print '0'
