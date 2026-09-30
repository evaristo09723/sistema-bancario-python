saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    print("\n===== SISTEMA BANCÁRIO =====")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação inválida! O valor deve ser maior que zero.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        if valor <= 0:
            print("Operação inválida! O valor deve ser maior que zero.")

        elif valor > saldo:
            print("Saldo insuficiente.")

        elif valor > limite:
            print("Operação inválida! O limite por saque é de R$ 500,00.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de 3 saques por dia atingido.")

        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n===== EXTRATO =====")

        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)

        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Sistema encerrado. Obrigado!")
        break

    else:
        print("Opção inválida. Escolha uma opção do menu.")