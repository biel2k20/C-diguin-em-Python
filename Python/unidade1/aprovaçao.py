# coding: utf-8
unidade = int(raw_input('Unidade? '))
media = float(raw_input('Média de aprovação na unidade? '))

proxima_unidade = unidade + 1
msg = 'O aluno vai para a unidade %d com média %.1f.'

print msg % (proxima_unidade, media)
