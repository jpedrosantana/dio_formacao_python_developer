def deposito(saldo, extrato):
    valor_deposito = float(input("Digite o valor a repositar R$..."))
    valor_saldo = saldo + valor_deposito
    status_extrato = extrato + f'Depósito de R$ {valor_deposito};\n'
    return valor_saldo, status_extrato

def ler_extrato(extrato, saldo):
    titulo = 'Extrato bancário'
    titulo_formatado = titulo.center(30, '=')
    print(titulo_formatado)
    print(extrato)
    print(f'\n\nTotal: {saldo}')
    print('=' * 30)

def sacar_dinheiro(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    limite = limite
    numero_saques = numero_saques
    saldo = saldo
    extrato = extrato
    LIMITE_SAQUES = LIMITE_SAQUES

    valor_saque = float(input("Digite o valor que você quer sacar R$..."))

    if numero_saques < LIMITE_SAQUES:
        if (valor_saque < limite) and (valor_saque <= saldo):
            numero_saques += 1
            saldo = saldo - valor_saque
            extrato = extrato + f'Saque de R$ {valor_saque};\n'
            print(f"Saque de {valor_saque} efetuado com sucesso, obrigado!")
        else:
            print("Valor inválido para essa operação. Verifique seu limite diário ou saldo disponível.")
            return extrato, saldo, numero_saques
    else:
        print("Número diário de saques já realizado, tente novamente em outro horário.")
        return extrato, saldo, numero_saques
    
    return extrato, saldo, numero_saques

'''
Função criar usuário (cliente):
Deve armazenar os clientes em uma lista.
Um usuário é composto por: nome, data de nascimento, cpf e endereço
O endereço é uma string com formato: logradouro, nro-bairro-cidade/sigla estado.
Não podemos cadastrar 2 usuários com o mesmo CPF
'''
def criar_usuario(usuario):
    cadastro = dict()
    nome = str(input("Informe o Nome: "))
    data_nascimento = str(input("Informe a data de nascimento: "))
    cpf = str(input("Informe o CPF: "))
    logradouro = str(input("Informe sua Rua: "))
    complemento = str(input("Informe o número, bairro e cidade/estado: "))

    cadastro['nome'] = nome
    cadastro['data de nascimento'] = data_nascimento
    cadastro['CPF'] = cpf
    cadastro['Endereço'] = [logradouro, complemento]

    for item in usuario:
        if item.get('CPF') == cpf:
            print("CPF já cadastrado")
            return usuario

    usuario.append(cadastro)

    print(f"Usuário {usuario[-1]['nome']} criado com sucesso!")

    return usuario

'''
Função criar conta corrente
Armazena as contas em uma lista, uma conta é composta por:
agência, número da conta e usuário. O número da conta é sequêncial,
iniciando em 1. O número da agência é fixo "0001". O usuário pode ter
mais de uma conta, mas uma conta só pode ter um usuário.
'''
def criar_conta(agencia, numero_conta, contas, usuario):
    nova_conta = list()
    vinculo_conta = str(input("Informe o CPF do titular da conta: "))

    for cliente in usuario:
        if vinculo_conta in cliente['CPF']:
            numero_conta = numero_conta + 1
            cliente['contas'] = nova_conta.extend([agencia, numero_conta])
            contas.append({'CPF': vinculo_conta, 'Conta': [agencia, numero_conta]})
            
        
    print(numero_conta)
    return usuario, numero_conta, contas

menu = '''
  [c] Criar Usuário
  [v] Criar Conta
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuario = list()
contas = list()
numero_conta = 0
LIMITE_SAQUES = 3
NUMERO_AGENCIA = "0001"

while True:
    opcao = input(menu)

    if opcao == 'd':
        saldo, extrato = deposito(saldo, extrato)
    
    elif opcao == 's':
        extrato, saldo, numero_saques = sacar_dinheiro(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

    elif opcao == 'e':
        ler_extrato(extrato, saldo)
    
    elif opcao == 'c':
        usuario = criar_usuario(usuario=usuario)

    elif opcao == 'v':
        usuario, numero_conta, contas = criar_conta(agencia=NUMERO_AGENCIA, numero_conta=numero_conta, contas=contas, usuario= usuario)
    
    elif opcao == 'q':
        print("Obrigado, essa operação está encerrada!")
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a opção desejada.')


