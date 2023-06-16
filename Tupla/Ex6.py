while True:
    inicio = int(input("Bem-vindo ao restaurante(digite 1 para continuar): "))
    if inicio == 1:
        break
pedidos = int(input("Digite o número de pedidos: "))
restaurante = []
for i in range(pedidos):
    nome = str(input("Digite o nome do pedido: "))
    qtd = int(input("Digite a quantidade disponível: "))
    preco = str(input("Digite o preço: "))
    tupla = (nome, qtd, preco)
    restaurante.append(tupla)
print(restaurante)