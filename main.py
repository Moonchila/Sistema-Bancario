import cpf
tot100=tot50=tot20=tot10=din=0
conta = 1001
saldo=500
nome=''
contc=1
cliente={}
clientes=[]

# PARA RODAR CORRETAMENTE E MANDATORIO CADASTRAR UM CLIENTE PRIMEIRO!!!
while True:
    print('-'*30)
    print(f'BANCO CARDOSO'.center(30))
    print('-'*30)
    print('Selecione uma opcao no MENU')
    print('''
    1- Criar Conta
    2- Efetuar Saque
    3- Efetuar Deposito
    4- Efetuar transferencia
    5- Listar Contas
    6- Sair do Sistema''')
    print('-='*25)
    opcao=0
    while opcao < 1 or opcao > 6:
        opcao=int(input('Opcao Selecionada: '))
    if opcao == 1:
        print('Informe os dados do cliente')
        cliente['nome']=input('Nome do Cliente: ').strip()
        cliente['email']=input('E-mail do Cliente: ').strip()
        #verificacao e-mail
        cliente['cpf']=(input('CPF do Cliente: '))
        cpf.cpf(cliente['cpf'])
        cliente['nascimento']=input('Data de nascimento do cliente: ')
        cliente['saldo']=float(input('Deposito Inicial para abertura de conta R$'))
        cliente['conta']=1000+contc
        clientes.append(cliente.copy())
        contc+=contc
        print('Conta criada com sucesso')
        print('-'*30)
        print(f'Numero da conta: {cliente["conta"]}')
        print(f'Nome do cliente: {cliente["nome"]}')
        print(f'Saldo Total: R${cliente["saldo"]}')

    elif opcao ==2:
        print('Esta maquina possui apenas notas de 10,20,50 e 100')
        valor=int(input('Qual o valor do saque? £'))
        cliente['saldo']-= valor
        if valor <= cliente['saldo']:
            while True:
                while valor >= 100:
                    valor=valor-100
                    tot100+=1

                else:
                    while valor >=50:
                        valor-=50
                        tot50+=1
                    else:
                        while valor >=20:
                            valor=valor-20
                            tot20+=1
                        else:
                            while valor>=10:
                                valor-=10
                                tot10+=1
                if tot10 >0:
                    print(f'cedulas de 10: {tot10}')
                if tot20 >0:
                    print(f'cedulas de 20: {tot20}')
                if tot50 >0:
                    print(f'cedulas de 50: {tot50}')
                if tot100 >0:
                    print(f'cedulas de 100: {tot100}')
                if valor ==0:
                    break

            print(f'Saldo total: R${cliente["saldo"]}')
        else:
            print('SALDO INSUFICIENTE')


    elif opcao ==3:
        cont=int(input('Informe o numero da conta: '))
        deposito=int(input('Informe o valor do deposito: R$'))
        if cont == cliente['conta']:
            cliente['saldo']+=deposito
            print(f'Deposito efetuado com sucesso!!')
        else:
            print('Conta incorreta!')
        print(f'Saldo atual: R${cliente["saldo"]}')
    elif opcao == 4:
        cont=int(input('Informe o numero da conta: '))
        dest=int(input('Informe a conta de desino: '))
        if cont == cliente['conta']:
            transf=int(input('Informe o valor da tranferencia: R$'))
            if transf <= cliente['saldo']:
                cliente['saldo']-=transf
            else:
                print('valor acima do saldo')
            print(f'Transferencia efetuada com sucesso!!')
            print(f'Saldo atual: R${cliente["saldo"]}')
        else:
            print('Conta Incorreta')
    elif opcao ==5:
        print('Listagem da conta')
        print(f'Numero da conta: {cliente["conta"]}')
        if len(cliente) == 0:
            print('Nao Ha cliente cadastrado')
        else:
            print(f"Nome do cliente: {cliente['nome']}")
            print(f'Saldo Total: R${cliente["saldo"]}')
    if opcao==6:
        print('Obrigado volte sempre!!')
        break



