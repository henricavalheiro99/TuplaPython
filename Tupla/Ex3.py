while True:
    inicio = int(input("Bem-vindo ao organizador de eventos(digite 1 para continuar): "))
    if inicio == 1:
        break
numero = int(input("Digite o número de eventos: "))
evento = []
for i in range(numero):
    nome = str(input("Digite o nome do evento: "))
    data = int(input("Digite o dia: "))
    local = str(input("Digite o local: "))
    tupla = (nome, data, local)
    evento.append(tupla)
print(evento)