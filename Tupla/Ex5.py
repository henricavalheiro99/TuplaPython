while True:
    inicio = int(input("Bem-vindo ao organizador de estoque(digite 1 para continuar): "))
    if inicio == 1:
        break
produtos = int(input("Digite o número de produtos: "))
informacoes = []
for i in range(produtos):
    nome = str(input("Digite o nome do produto: "))
    qtd = int(input("Digite a quantidade disponível: "))
    preco = str(input("Digite o preço: "))
    tupla = (nome, qtd, preco)
    informacoes.append(tupla)
print(informacoes)