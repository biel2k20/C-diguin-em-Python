#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Cálculo do IMC

peso = float(raw_input())
altura = float(raw_input())
imc = peso / (altura ** 2)
if imc < 16:
	print 'IMC: %.1f - Magreza grave' % (imc)
elif 16 <= imc < 17:
	print 'IMC: %.1f - Magreza moderada' % (imc)
elif 17 <= imc < 18.5:
	print 'IMC: %.1f - Magreza leve' % (imc)
elif 18.5 <= imc < 25:
	print 'IMC: %.1f - Saudável' % (imc)
elif 25 <= imc < 30:
	print 'IMC: %.1f - Sobrepeso' % (imc)
elif 30 <= imc < 35:
	print 'IMC: %.1f - Obesidade Grau I' % (imc)
elif 35 <= imc < 40:
	print 'IMC: %.1f - Obesidade Grau II (severa)' % (imc)
elif 40 <= imc:
	print 'IMC: %.1f - Obesidade Grau III (mórbida)' % (imc)
