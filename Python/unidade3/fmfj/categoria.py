#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: categoria

nome = raw_input()
idade = int(raw_input())

if idade < 5:
	print '%s, %d anos, Não pode competir.' % (nome, idade)
elif 5 <= idade <= 7:
	print '%s, %d anos, Infantil A.' % (nome, idade)
elif 8 <= idade <= 10:
	print '%s, %d anos, Infantil B.' % (nome, idade)
elif 11 <= idade <= 13:
	print '%s, %d anos, Juvenil A.' % (nome, idade)
elif 14 <= idade <= 17:
	print '%s, %d anos, Juvenil B.' % (nome, idade)
elif idade > 17:
	print '%s, %d anos, Senior.' % (nome, idade)
