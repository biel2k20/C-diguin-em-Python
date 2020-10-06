#coding: utf-8
#Gabriel Dantas Santos de Azevêdo
#Matrícula: 118210140
#Problema: Fila por Altura

def insere_na_fila(fila,nome,altura):
	x = (nome, altura)
	fila.append(x)
	for i in range(len(fila) - 1, 0, -1):
		if fila[i][1] < fila[i-1][1]:
			fila[i], fila[i-1] = fila[i-1], fila[i]
        
	return fila

