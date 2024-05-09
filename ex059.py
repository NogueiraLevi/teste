from time import sleep  # Importa a função sleep do módulo time

print("Bem-vindo ao programa de cálculos!")

# Solicita que o usuário digite dois números e armazena esses números em n1 e n2
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
opcao = 0  # Inicializa a variável de opção com 0

# Começa um loop que continuará até que o usuário escolha sair do programa (opcao = 5)
while opcao != 5:
    print("""
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    """)
    opcao = int(input("Escolha uma opção: "))  # Solicita ao usuário que escolha uma opção

    # Verifica qual opção foi escolhida pelo usuário
    if opcao == 1:  # Se a opção for 1, realiza a soma
        soma = n1 + n2
        print("A soma entre {} e {} é {}".format(n1, n2, soma))
    elif opcao == 2:  # Se a opção for 2, realiza a multiplicação
        produto = n1 * n2
        print("O produto entre {} e {} é {}".format(n1, n2, produto))
    elif opcao == 3:  # Se a opção for 3, encontra o maior número
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {}, o maior é {}".format(n1, n2, maior))
    elif opcao == 4:  # Se a opção for 4, permite ao usuário inserir novos números
        print("Digite os novos números: ")
        n1 = int(input("Novo N1: "))
        n2 = int(input("Novo N2: "))
    elif opcao == 5:  # Se a opção for 5, informa que o programa está finalizando
        print("Finalizando...")
    else:  # Se a opção não for válida, informa ao usuário que é inválida
        print("Opção Inválida!! Tente Novamente")

    sleep(2)  # Aguarda 2 segundos antes de continuar para dar tempo ao usuário de ler as mensagens

print("Fim do programa. Volte Sempre!!")  # Informa ao usuário que o programa está finalizado
