menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print("Falha na operação. O valor informado é inválido.")    

    elif opcao == "s":
        
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > saldo

        excedou_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente para realizar esta operação.")

        elif excedou_limite:
            print(f"Valor excede o limite por saque de {limite}.")

        elif excedeu_saque:
            print(f"Número diário de {LIMITE_SAQUES} excedido.")

        if valor > 0:
            saldo -= valor
            extrato += f'saque: R${valor:.2f}\n'
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")                

    elif opcao == "e":
        print("\n##########EXTRATO###########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("##############################")

    elif opcao == "q":
        break


    else:
        print("Operação inválida, por favor selecione uma das operações disponibilizadas.")    
        