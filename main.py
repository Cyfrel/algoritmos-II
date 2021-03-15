

lista_nome = ['caneta','xicara','garfo','garrafa']
lista_preco = [3,15,12,5]
lista_quantidade = [1,2,7,8]



print("Produtos Armazenados:", lista_nome)
nome = input("selecione um produto a ser printado ou apagado:\n")
selecao = input("1 - selecionar 2 - apagar:\n")

if selecao == '1':
    for i in range (len(lista_nome)):
        if lista_nome[i] == nome: 
            print(lista_nome[i])
            print(lista_preco[i])
            print(lista_quantidade[i])

if selecao == '2':
    for i in range (len(lista_nome)):
        if lista_nome[i] == nome: 
            lista_nome[i].pop 