#coding: utf-8

a = int(raw_input())
range(a)
l = []
d = []
t = []
for e in range(a):
	e = int(raw_input())
	l.append(e)
for x in l:
	if 10 <= x <= 20:
		d.append(x)
	else:
		t.append(x)
print '%d in' % len(d)
print '%d out' % len(t)
