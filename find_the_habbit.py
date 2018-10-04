#nomes = ['Julio', 'Caio', 'Hugo', 'Eduardo', 'Diogo', 'Hector']

# Procurar pelo nome 'Hugo' e escrever na tela
# caso encontrado
# Escrever "Encontramos o Hugo pelado"

# procurar Mario, se mário n for encontrado, escrever, vc conhece o mario?

nomes = [
	{'nome' : 'Julio', 'idade' : 30},
	{'nome' : 'Caio', 'idade' : 29},
	{'nome' : 'Hugo', 'idade' : 24},
	{'nome' : 'Eduardo', 'idade' : 39},
	{'nome' : 'Diogo', 'idade' : 34},
	{'nome' : 'Hector', 'idade' : 27}]


for n in nomes:
    if n['nome'] == 'Mario':
        break
else:
    print('vc conhece o mario?')