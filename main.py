import os

LIMITE_SAQUES = 3
def menu():
    return int(input("""
######## Menu de Operações: ########
[1] Criar conta
[2] Listar Contas
[3] Depositar
[4] Sacar
[5] Saldo/Extrato
[6] Sair

Escolha uma das opções acima:
==> """));

def selecionar_conta(lista_contas):
    print()
    print("######## Selecionar Contas: ########")
    for i, _ in enumerate(lista_contas):
        print(i, lista_contas[i]['nome'], lista_contas[i]['numero'])
    conta_selecionada = input("Selecione sua conta: ")
    if conta_selecionada == '':
        invalid()
        return selecionar_conta(lista_contas)
    if int(conta_selecionada) < 0 or int(conta_selecionada) >= len(lista_contas): 
        invalid()
        return selecionar_conta(lista_contas)
    return int(conta_selecionada)

def listar_constas(lista_contas):
    console_clear()
    print("######## Listar Contas: ########")
    for i, _ in enumerate(lista_contas):
        print(lista_contas[i]['nome'], lista_contas[i]['numero'])
    return
    
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def insert_valor(texto):
    valor = float(input(texto+ ' '))
    if valor < 0 or valor == '':
        insert_valor(texto)
    return valor

def depositar(conta, lista_contas):
    console_clear()
    print(f"######## Depositar para conta {lista_contas[conta]['numero']} ########")
    valor = insert_valor(("Quanto deseja depositar? "))
    lista_contas[conta]['saldo'] += valor
    lista_contas[conta]['extrato'] += f"Deposito: R$ {valor:.2f}\n"
    print(f'################# DEPOSITO REALIZADO COM SUCESSO  #################\n\n')
    print(f"Deposito de R$ {valor:.2f} realizado com sucesso na conta {lista_contas[conta]['numero']}")
    return lista_contas

def sacar(conta, lista_contas):
    console_clear()
    print(f"######## Sacar da conta {lista_contas[conta]['numero']} ########")
    global LIMITE_SAQUES
    valor = insert_valor(("Quanto deseja sacar? "))
    excedeu_saldo = valor > lista_contas[conta]['saldo']
    excedeu_limite = valor > lista_contas[conta]['limite']
    if excedeu_saldo:
        console_clear()
        invalid("Saldo insuficiente")
    elif excedeu_limite:
        console_clear()
        invalid(f"Limite de R$ {lista_contas[conta]['limite']:.2f} excedido")
    elif lista_contas[conta]['numero_saques'] > LIMITE_SAQUES:
        console_clear()
        print("Limite de saques excedido")
    elif valor > 0:
        lista_contas[conta]['saldo'] -= valor
        lista_contas[conta]['extrato'] += f"Saque: R$ {valor:.2f}\n"
        print(f'################# SAQUE REALIZADO COM SUCESSO  #################\n\n')
        print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {lista_contas[conta]['numero']}")
    else:
        console_clear()
        invalid()
    return lista_contas
        
def saldo_extrato(conta, lista_contas):
    print("Seu saldo: R$ {:.2f}".format(lista_contas[conta]['saldo']))
    print("Seu extrato: \n{}".format(lista_contas[conta]['extrato']))
    return lista_contas
def criar_conta(lista_contas):
    console_clear()
    print("######## Criar Conta: ########")
    conta = {};
    conta['nome'] = str(input("Insira o nome do proprietário: "))
    conta['numero'] = str(len(lista_contas) + 1).zfill(5)
    conta['saldo']= 0
    conta['limite'] = 500
    conta['extrato'] = ""
    conta['numero_saques'] = 0
    print("Conta criada com sucesso!")
    return conta
 
def next():
     input('\nPressione <enter> para continuar')
def invalid(text = "Opção invalida"):
    print(text)
def init_banco():
    lista_contas = []
    while True:
        console_clear()
        opcao = menu()
        match opcao:
            case 1: # criar conta
                lista_contas.append(criar_conta(lista_contas))
            case 2: # Listar Contas
                if(len(lista_contas) == 0):
                    print("Nenhuma conta criada")
                else:
                    listar_constas(lista_contas) 
                    
            case 3: #Depositar
                if(len(lista_contas) == 0):
                    print("Primeiro, crie uma conta")
                    lista_contas.append(criar_conta(lista_contas))
                    lista_contas = depositar(0,lista_contas)
                else:
                    conta_selecionada = selecionar_conta(lista_contas)
                    lista_contas = depositar(conta_selecionada,lista_contas)
                
            case 4: #Sacar
                if(len(lista_contas) == 0):
                   print("Nenhuma conta criada")
                else:
                    conta_selecionada = selecionar_conta(lista_contas)
                    lista_contas = sacar(conta_selecionada,lista_contas)
                    
            case 5:
                console_clear()
                if(len(lista_contas) == 0):
                    print("Nenhuma conta criada")
                else:
                    conta_selecionada = selecionar_conta(lista_contas)
                    lista_contas = saldo_extrato(conta_selecionada,lista_contas)   
            case 6: 
                console_clear()
                print("Saindo...")
                break;
            case _:
                console_clear()
                invalid()
        next()
        console_clear()


if __name__ == '__main__':
    init_banco()