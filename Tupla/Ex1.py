while True:
    inicio = int(input("Bem-vindo ao organizador de amigos(digite 1 para continuar): "))
    if inicio == 1:
        break
numero = int(input("Digite o número de amigos: "))
amigos = []
for i in range(numero):
    nome = str(input("Digite o nome do amigo: "))
    idade = str(input("Digite a idade do amigo: "))
    tupla = (nome, idade)
    amigos.append(tupla)
print(amigos)