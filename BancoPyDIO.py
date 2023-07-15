from datetime import datetime
import textwrap

def menu():
    menu = '''
[d]\tDepositar
[s]\tSacar
[e]\tExibir Extrato
[nc]\tCriar nova conta
[lc]\tListar contas
[nu]\tCriar novo usuário
[q]\tSair das operações

'''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += str(datetime.now()) + f"\n\tDepósito de R$ {valor:.2f} "
        print('Depósito realizado ')
    else:
        raise ValueError("Valor inválido para depósito")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n\tA quantia solicitada ultrapassa seu saldo disponível.')
    elif excedeu_limite:
        print('\n\tA quantia solicitada ultrapassa sua cotação máxima diária.')
    elif excedeu_saques:
        print('\n\tLimite de saques atingido.')
    elif valor > 0:
        print ('\tValor em conta suficiente para sacar.')
        saldo -= valor
        extrato += f'\tSaque no valor de R$ {valor:.2f}'
        numero_saques += 1
        print('\tSeus novos valores são: ')
    else:
        print ('\tFunção ou valor inválidos.')

    return saldo, extrato

def exibirExtrato(saldo, extrato):
    print(' ---------- Extrato: --------- ')
    print(f'\tNão foram realizadas movimentações' if not extrato else extrato)
    print(f'\tO saldo é de R$ {saldo:.2f}')
    print(' ----------------------------- ')

def criarUsuario(usuarios):
    print("\t-----Criando usuário--------")
    cpf = input("\tInforme seu CPF utilizando apenas números: ")
    usuario = filtrarUsuario(cpf, usuarios)
    if usuario:
        print("\t---- Operação inválida! ------")
        print("\t Já existe usuário cadastrado com esse CPF")
        return
    print("Vamos iniciar o cadastro do novo usuário")
    nome = input("Nome completo do Usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário no formato dd/mm/aaaa: ")
    endereco = input("Digite a rua/logradouro, cidade e iniciais do estado: ")
    usuarios.append({'Nome': nome, 'data_nascimento': data_nascimento, 'CPF': cpf, 'endereço': endereco})
    print('\tUsuário criado com sucesso!')

def filtrarUsuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['CPF'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criarConta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrarUsuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso.")
        return {"Agência número: ": agencia, "Número da conta: ": numero_conta, "Usuário": usuario}
    print("Usuário não encontrado, favor realizar cadastro!")

def listarContas(contas):
    for conta in contas:
        linha = f'''Agência:\t {conta['Agência número']}
        \tC/C:\t\t {conta['Número da conta']}
        \tTitular:\t {conta['Usuário']['Nome']}'''
        print('\t----------------------------------')
        print(textwrap.dedent(linha))

def main():
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input('\tQual valor será depositado? '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('\tQual valor deseja sacar? '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques
            )
        elif opcao == 'e':
            exibirExtrato(saldo, extrato)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criarConta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                print("\tConta criada com sucesso!")

        elif opcao == 'lc':
            listarContas(contas)

        elif opcao == 'nu':
            criarUsuario(usuarios)

        elif opcao == 'q':
            break

        else:
            print('\tOpção inválida')

if __name__ == '__main__':
    main()