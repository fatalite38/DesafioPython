
#Exibindo o Menu para interação do usuário
menu = """
================Bem-vindo Cliente ================

Escolha uma opção:
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

=> """

#Declarando as Variáveis utilizadas
saldo = 0
limite = 2000
extrato = ""
numeroSaques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    # opção para o usuário depositar uma quantia em dinheiro
    if opcao == 'd':
        valor = float(input("Informe o valor a ser depositado: R$"))
        
    #Verifica se o valor é valido, ou seja, se é maior que zero.
        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R${valor:.2f}\n"
        else:
            print("\nValor inválido!")
    
    # Opção para o usuario Sacar uma quantia em dinheiro
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: R$"))

        # Verifica se o valor do saque excede o saldo na conta
        excedeuSaldo = valor > saldo

        # Verifica se o valor do saque ultrapassa o valor limite
        excedeuLimite = valor > limite

        # Verifica se o número de saques diários foi ultrapassado
        excedeuSaques = numeroSaques >= LIMITE_SAQUES

        if excedeuSaldo:
            print("Você não possui esse valor em sua conta.")
        
        elif excedeuLimite:
            print("Você ultrapassou o valor de saque.")

        elif excedeuSaques:
            print("Você já realizou o número máximo de saques diários permitidos.")
        
        #Verifica se o valor é valido, ou seja, se é maior que zero.
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeroSaques += 1
        
        else:
            print("Valor informado é inválido.")
    
    #Opção para o usuário visualizar o extrato
    elif opcao == "e":
        print("\n================Extrato================")
        #Se não houver transações, imprima uma mensagem!
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
    
    # Opção para o usuário Sair do programa.
    elif opcao == "q":
        break
    else:
        print("\nOpção Inválida!\nTente novamente.")

