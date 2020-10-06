#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Avaliação Docente

semestre = float(raw_input())
p_ensino = float(raw_input())
p_intelectual = float(raw_input())
p_orientacao = float(raw_input())
p_administrativas = float(raw_input())

if semestre < 4:
	print 'Promoção indeferida. Número de semestres insuficiente.'
elif semestre >= 4:
	if p_ensino < 320 or p_intelectual < 100 or p_orientacao < 20:
		print 'Promoção indeferida. Pontuação mínima não alcançada.'
	elif p_ensino >= 320 and p_intelectual >= 100 and p_orientacao >= 20:
		media = (p_ensino + p_intelectual + p_orientacao + p_administrativas) / 4
		if media >= 140:
			print 'Promoção deferida. Parabéns!'
		else:
			print 'Promoção indeferida. Média insuficiente.'
