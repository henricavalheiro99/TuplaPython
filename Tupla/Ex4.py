while True:
    inicio = int(input("Bem-vindo à lista telefônica (digite 1 para continuar): "))
    if inicio == 1:
        break
contatos = int(input("Digite o número de contatos: "))
lista = []
for i in range(contatos):
    nome = str(input("Digite o nome: "))
    telefone = int(input("Digite o telefone: "))
    email = str(input("Digite o email: "))
    tupla = (nome, telefone, email)
    lista.append(tupla)
print(lista)