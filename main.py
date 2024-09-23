menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
log_movimentacoes = []

def depositar(valor_deposito):
    global saldo, log_movimentacoes
    
    if valor_deposito>=0:

        saldo += valor_deposito

        #adicionar o log do depósito no final da lista
        log_movimentacoes.append(f"Depósito: R$ {valor_deposito:.2f}")
        print("Depósito realizado")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
        return saldo
    
    else:
        print("Valor informado inválido")
    

def sacar(valor_saque):
    global saldo, numero_saques

    if numero_saques<LIMITE_SAQUES:

        if valor_saque>=0:
            
            if valor_saque<=saldo:
                if valor_saque<=limite:
                    saldo -= valor_saque

                    #adicionar o log do saque no final da lista
                    log_movimentacoes.append(f"Saque: R$ {valor_saque:.2f}")
                    print("Saque realizado")
                    print(f"Seu novo saldo é: R$ {saldo:.2f}")
                    numero_saques += 1
            
                    return saldo
                else:
                    print(f"Valor do saque maior que o limite disponível (Limite atual: R$ {limite:.2f})\nSaque não realizado!")
                    
            
            else:
                print(f"Valor do saque maior que o saldo disponível (Saldo atual: R$ {saldo:.2f})\nSaque não realizado!")

        else:
            print("Valor informado inválido")
    else:
        print("Limite de saques diários já foi atingido")


def exibir_extrato():
    print("\n=========== Extrato ===========\n")

    #visualizar o log de movimentações linha por linha
    for exibicao_extrato in log_movimentacoes:
        print(exibicao_extrato)
    
    print(f"Saldo atual: R$ {saldo:.2f}")


while True:

    opcao = input(menu + "Digite a opção desejada e aperte enter: ")

    if opcao == "1":

        #receber o valor de depósito para executar a função
        depositar(valor_deposito= float(input("Digite o valor de depósito: R$ ")))
        

    elif opcao == "2":

        #receber o valor de saque para executar a função
        sacar(valor_saque= float(input("Digite o valor de saque: R$ ")))
        
    elif opcao == "3":
        exibir_extrato()
    
    elif opcao == "0":
         break
    
    else:
         print("Opção inválida. Digite uma opção válida")

print("\nSistema bancário finalizado")