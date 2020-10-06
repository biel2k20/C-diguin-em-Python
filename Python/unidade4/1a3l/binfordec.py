#coding: utf-8	
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140t
#Problema: B2 para B10

binario = raw_input()

soma = 0
valores = [1,2,4,8,16,32,64,128,256,512,1024,2048]
valor = valores[len(binario)-1]
for bit in range(len(binario)):
		conta = int(binario[bit]) * valor
		print '%d * %d = %d' % (int(binario[bit]), valor, conta)
		soma += conta
		valor /= 2

print '%s(2) = %d(10)' % (binario, soma)
