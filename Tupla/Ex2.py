while True:
    inicio = int(input("Bem-vindo ao organizador de números(digite 1 para continuar): "))
    if inicio == 1:
        break
numeros = (4, 5, 8, 9, 2, 3, 1, 0)
print(sorted(numeros))