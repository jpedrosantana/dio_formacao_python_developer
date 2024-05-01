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


menu = '''
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        saldo, extrato = deposito(saldo, extrato)
    
    elif opcao == 's':
        extrato, saldo, numero_saques = sacar_dinheiro(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

    elif opcao == 'e':
        ler_extrato(extrato, saldo)
    
    elif opcao == 'q':
        print("Obrigado, essa operação está encerrada!")
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a opção desejada.')


