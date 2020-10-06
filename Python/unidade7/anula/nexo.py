#coding:utf-8

def anula(l):
	k = len(l)
	while True:
		k -= 1
		if len(l) > 1:
			if l[k] + l[k-1] == 0:
				l.pop(k), l.pop(k-1)
				k = len(l)-1
			if k == -1:
				break
		else:
			break
