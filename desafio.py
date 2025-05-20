saldo = 1500
limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

while True:
    print("\n=== MENU ===")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES_DIARIOS:
            print("Limite diário de saques atingido.")
            continue

        valor = float(input("Informe o valor do saque: R$ "))
        
        if valor <= 0:
            print("Operação falhou! Valor inválido.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite_saque:
            print("Operação falhou! O valor do saque excede o limite de R$ 500.00.")
        else:
            saldo -= valor
            extrato.append(f"Saque:    R$ {valor:.2f}")
            numero_saques += 1
            print("Saque realizado com sucesso.")

    elif opcao == "e":
        print("\n==== EXTRATO ====")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in extrato:
                print(movimento)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=================")

    elif opcao == "q":
        print("Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
