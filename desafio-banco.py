opcoes = f""" 
    [0] cancelar
    [1] Depósito
    [2] saque
    [3] extrato
    (Não é possível realizar saques acima de R$500,00 e mais de 3 vezes no mesmo dia)
    """
print (opcoes)

saldo = 0
extrato_deposito = 0
extrato_saque = 0
escolha = 0



while (escolha != -1 and escolha <=3):
    escolha = int(input("Qual a opção desejada:"))
    if escolha == 0:
        print ("A operação está sendo encerrada!")
        exit()
    elif escolha == 1:
        deposito = float(input("Insira o valor que você deseja depositar: "))
        saldo += deposito
        if deposito > 0:
            extrato_deposito += deposito
            print (f"Saldo: R${saldo}")

    elif escolha == 2:
        saque = float(input("Quanto você gostaria de sacar? "))
        numero_saque = 0
        if saldo < saque : 
            mensagem = str(input("Infelizmente você não tem esse valor disponivel!"))
        elif saque > 500 or numero_saque >= 3:
            print ("Não é possível realizar o saque, consulte o nosso regulamento!")
        else :
            numero_saque += 1
            extrato_saque += saque
            saldo -= saque
            print (F"Saque realizado com sucesso! Saldo: R${saldo}")

    else :
        if extrato_deposito==0 and extrato_saque==0:
            print("Não foram realizadas movimentações!")
        elif escolha >= 4:
            print ("Está opção não está disponível!")
        else :
            print ("Extrato:")
            print (f"Total de depósitos: R${extrato_deposito}")
            print (f"Saque: R${extrato_saque}")
            print (f"Saldo: R${saldo}")      
