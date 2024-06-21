'''
Atividade somativa:
Estevan R. Tomazini
Curso de BigData e inteligência analítica
Disciplina de Raciocínio Computacional
Professor tutor - Wellington Monteiro

'''

import json

## Da semana 7 para a 8 a carga de trabalho e pensar como fazer 
## foi bastante pesado
## Mas esse novo modelo da disciplina está mais útil, no tempo 
## do zombie dice não tinhamos essa parte de leitura e criação
## de arquivos e parece realmente útil para quem tiver oportunidade 
## de ser dev.

# Parte da Somativa I: transformar em funções:
def menu():
    '''
    Mostra a tela inicial do programa de cadastro 
    secretaria. Não inclui argumentos.

    '''
    print ('------------------------------------------------')
    print ('\tBem-Vindo ao: ')
    print ('\tPROGRAMA DE ASSUNTOS ESTUDANTIS')
    print ('-------------------------------------------------')
    print ('\n\tMENU PRINCIPAL:  ')
    print(' \n\t[1] GERENCIAR ESTUDANTES.') #opção 1 
    print(' \n\t[2] GERENCIAR DISCIPLINAS.') #opção 2
    print(' \n\t[3] GERENCIAR PROFESSORES.') #opção 3 
    print(' \n\t[4] GERENCIAR TURMAS.') #opção 4
    print(' \n\t[5] GERENCIAR MATRICULAS.') #opção 5
    print(' \n\t[9] SAIR.') #opção 9
    print ('-------------------------------------------------')
    opcao = int(input(" Informe a opção desejada: "))
    return opcao

def menu_secundario (opcao_1):
    '''
    Mostra menu secundário, de atividades, após seleção da opção inicial
    
       
    '''
    print('-------------------------------------------------')
    print("\t-----["+opcao_1+"] Menu de tarefas -----\n")
    print('-------------------------------------------------')
    print('\n\tCÓDIGO DAS TAREFAS ESTÁ LISTADO A SEGUIR: \n')
    print("\n\t[1] --- INCLUIR --- ")
    print("\n\t[2] --- LISTAR --- ")
    print("\n\t[3] --- ATUALIZAR --- ")
    print("\n\t[4] --- EXCLUIR --- ")
    print("\n\t[9] --- RETORNAR AO MENU PRINCIPAL --- \n")
    print('-------------------------------------------------')
    opcao_2 = int(input(" Digite a opção da tarefa a ser realizada:  ")) 
    return opcao_2

def incluir ():
    '''
    Inclui estudante na lista 'Estudantes.json'
    1 - pede codigo, nome e CPF
    2 - agrupa em formato de dicionário
    3 - extende a lista de dicionarios via append()
    '''
    print("\n\t--- opção selecionada -> INCLUSÃO de aluno ---\n")
    codigo = int(input("\n\tDigite o --- CÓDIGO --- do aluno: \n"))
    nome =  str(input("\n\tDigite o --- NOME --- do aluno: \n"))
    cpf = str(input("\n\tDigite o --- CPF --- do aluno: \n"))

    dicionario = {
        'codigo': codigo,
        'nome': nome ,
        'cpf': cpf
    }

    dados = recuperar_arquivo()
    dados.append(dicionario)
    salvar_arquivo(dados)
    input("\n aperte <ENTER> \n") ## realmente gostei do input para isso

def listar ():
        '''
        lista dados presentes no dicionário para alunos
        1 - Lê os dados presentes
        2 - Percorre estudantes e imprime
        '''
        print("\n\t--- opção selecionada -> LISTAGEM de aluno ---\n")
        dados = recuperar_arquivo()
        if len(dados) < 1:
            print("\n\tAinda não existe ESTUDANTES CADASTRADOS\n")
            input('aperte <ENTER>')
        else:
            
            print("Código do aluno \tNome do aluno \tCPF do aluno ")
            for estudante in dados:
                print(str(estudante['codigo']) + "\t" + estudante['nome'] + "\t" + estudante['cpf'])
                    
        input("\nAperte <ENTER> ")
    
def atualizar ():
    '''
    Deve testar caso o código do aluno exista,
    se não existir, indicará "não registrado"
    se existir, pedirá codigo, nome e CPF.
    '''
    print("\n\t--- opção selecionada: ATUALIZAÇÃO de Aluno ---\n")
    dados = recuperar_arquivo ()
    codigo = int(input("Digite o código do aluno que deseja ATUALIZAR: "))


    contem = False
    for iteravel in dados:
        if iteravel['codigo'] == codigo:
         
    
            codigo = int(input("Digite novo código do estudante: "))
            nome = input("Digite novo nome do estudante: ")
            cpf = input("Digite novo CPF do estudante: ")

            # Edita dicionário
            iteravel['codigo'] = codigo
            iteravel['nome'] = nome
            iteravel['cpf'] = cpf
                        
            contem = True
            break
        
    if not contem:
        print("\n\tAluno não registrado.")
    else:
        # Salva dados atualizados no arquivo
        salvar_arquivo(dados)

    input("\n\tAperte <ENTER> ")

def excluir ():
    '''
    exclui arquivo dado código do aluno:
    1 - entrado do código do aluno a se excluir
    2 - itera na lista e deleta caso contenha
    3 - Caso tenha percorrido a lista e não encontrado, mostra mensagem
    4 - Salva dados atualizados no arquivo

    '''
    print("\n\t--- opção selecionada: EXCLUSÃO de Aluno ---\n")
    dados = recuperar_arquivo()
    codigo = int(input("Informe o código do estudante para exlusão: "))

    contem = False
    for iteravel in dados:
        if iteravel['codigo'] == codigo:
            dados.remove(iteravel)
            contem = True
            break

    if not contem:
        print("\nRegistro não encontrado.")
    else:
        salvar_arquivo(dados)
    input("\nPressione <ENTER> para continuar.")

def recuperar_arquivo ():
    '''
    Abre 'Estudantes.json':
    - Se existir retorna os registros lidos como uma lista;
    - Senao retorna dados da lista
    '''
    try :
        with open('estudantes.json', 'r') as file:
            dados = json.load(file)
         
    except FileNotFoundError:
        dados = []
    return dados

def salvar_arquivo(dados):
    '''
    1 - abre o arquivo 'Estudantes.json' no modo escrita 'w'
    2 - Transforma lista de dicionários em JSON 
    '''
    with open('Estudantes.json', 'w') as file: 
        json.dump(dados, file) 


## Somativa 2:

# Lógica do programa
# iniciei tentando fazer esse modelo de modularidade MAS
# a 2º opção não funcionou como o esperado, tinha ajustado
# todas as funções para que o comentário funcionasse 
# dessa forma, o código acabou ficando monolítico

# no final do script, copiarei a versão anterior das funções
## Essa aqui era a estruturação da versão anterior

'''
opcao = 1
while opcao != 9:

    # Chama função para montagem do menu principal
    # Retorna opção escolhida pelo usuário
    opcao = menu ()

    opcao_1 = ""
    if opcao == 1:
        opcao_1 = "ESTUDANTES"
        if opcao_2 == 1:
            incluir ()
        if opcao_2 == 1:
            listar ()
        if opcao_2 == 1:
            atualizar ()
        if opcao_2 == 1: 
            excluir ()
        if opcao_2 == 9:
            break

    elif opcao == 3:
        opcao_1 = "PROFESSORES"
        if opcao_2 == 1:
            incluir_professor ()
        if opcao_2 == 2:
            listar_professor ()
        if opcao_2 == 3:
            atualizar_professor ()
        if opcao_2 == 4:
            excluir_professor ()
        if opcao_2 == 9:
            break

    elif opcao == 2:
        opcao_1 = "DISCIPLINAS"
        if opcao_2 == 1:
            incluir_disciplina ()
        if opcao_2 == 2:
            listar_disciplina ()
        if opcao_2 == 3:
            atualizar_disciplina ()
        if opcao_2 == 4:
            excluir_disciplina ()
        if opcao_2 == 9:
            break
       
    elif opcao == 4:
        opcao_1 = "TURMAS"
        # Seleciona a opção 4 do menu principal
        opcao = 4
        if opcao_2 == 1:
            incluir_turma ()
        if opcao_2 == 1:
            atualizar_turma()
        if opcao_2 == 1:
            listar_turma ()
        if opcao_2 == 1:
            excluir_turma ()
        if opcao_2 == 9:
            break

    elif opcao == 5:
        opcao_1 = "MATRICULAS"
        if opcao_2 == 1:
            atualizar_turma ()
        if opcao_2 == 1:
            listar_matricula ()
        if opcao_2 == 1:
            incluir_matricula ()
        if opcao_2 == 1:
            excluir_turma ()
        if opcao_2 == 9:
            break

    elif opcao == 9:
        break
    else:
        print("\n\nOpção incorreta!\n\n")
        input("Pressione ENTER para continuar.")
        continue
'''

## menu secundário

opcao_2 = 1
while opcao_2 != 9:
    opcao = menu()
    if opcao == 1:
        opcao_1 = "Alunos"


    elif opcao ==3:
        '''
        polimorfismos para a opção professor

        '''
        opcao_1 = "Professores" 

        def incluir():
            print (" opção selecionada -> INCLUSÃO de Professores: ")

            ## def incluir_professor (): 
            '''
            1 - Inclui um novo professor no sistema.
            2 - Solicita ao usuário os dados do professor
            3 - Cria um dicionário com os dados do professor
            4 - Salva o professor no arquivo

            '''
            codigo = int(input("\n\tDigite o código do professor: \n"))
            nome = input("\n\tDigite o nome do professor: \n")
            cpf = input("\n\tDigite o CPF do professor: \n")
            dicionario = {
                "codigo": codigo,
                "nome": nome,
                "cpf": cpf
            }

            dados = recuperar_arquivo()
            dados.append(dicionario)
            salvar_arquivo(dados)
            print("\n\tPROFESSOR incluído com sucesso.")
            input("\naperte <ENTER> ")

        def listar ():

            '''
            Lista todos os professores no sistema.
            Percorre estudantes e imprime

            '''
            dados = recuperar_arquivo()
            if len(dados) < 1:
                print("\n\tAinda não existe PROFESSORES CADASTRADOS\n")
                
            else:
                print("Código\tNome\tCPF")
            for professor in dados:
                print(str(professor['codigo']) + "\t" + professor['nome'] + "\t" + professor['cpf'])
            input("\nPressione ENTER para continuar.")

        def atualizar ():

            '''
            Atualiza os dados de um professor no sistema.
            1 - Solicita código do professor
            2 - Verifica se o codigo existe
            3 - Edita dicionário
            4 - Salva dados atualizados no arquivo

            '''
            print("\n\t--- opção selecionada -> ATUALIZAÇÃO de Professor ---\n")
            dados = recuperar_arquivo ()
            codigo = int(input("\n\tDigite o código do professor a ser atualizado: \n"))
            
            contem = False
            for iteravel in dados:
                if iteravel['codigo'] == codigo:
                
                    codigo = int(input("Informe o novo código do estudante: "))
                    nome = input("Informe o novo nome do estudante: ")
                    cpf = input("Informe o novo CPF do estudante: ")

                    iteravel['codigo'] = codigo
                    iteravel['nome'] = nome
                    iteravel['cpf'] = cpf
                                
                    contem = True
                    break
            if not contem:
                print("\nCódigo do professor não encontrado.")
            else:
                salvar_arquivo(dados)
            input("\nPressione <ENTER> para continuar.")

        def excluir ():

            '''
            Exclui um professor do sistema.
            1 - Solicita ao usuário o código do professor
            2 - Procura na lista e deleta caso ache
            3 - Caso tenha percorrido a lista e não encontrado, mostra mensagem
            4 - Salva dados atualizados no arquivo

            '''
            print("\n\t--- opção selecionada: EXCLUSÃO de Professor ---\n")
            dados = recuperar_arquivo ()
            codigo = int(input("\n\tDigite o código do professor a ser excluído: \n"))
            contem = False
            for iteravel in dados:
                if iteravel['codigo'] == codigo:
                    dados.remove(iteravel)
                    contem = True
                    break
            if not contem:
                print("\nRegistro não encontrado.")
            else:
                salvar_arquivo(dados)
            print("\n\tProfessor excluído com sucesso.")
            input("\nPressione <ENTER> para continuar.")

        def recuperar_arquivo ():
            '''
            O mesmo do que a função nativa, com o arquivo 'Professores'
            '''
            try :
                with open('Professores.json', 'r') as file:
                    dados = json.load(file)
            except FileNotFoundError:
                dados = []
            return dados
       
        def salvar_arquivo(dados):
            with open('Professores.json', 'w') as file: 
                json.dump(dados, file) 

    elif opcao == 2:
        opcao_1 = "Disciplinas"

        '''
        Polimorfismos da opção disciplinas:
        '''

        def incluir ():
            '''
            Inclusão de disciplina
            1 - Cria um dicionário com os dados da disciplina
            2 - Salva a disciplina no arquivo
            3 - Exibe uma mensagem de sucesso

            '''
            codigo = int(input("\n\tDigite o código da disciplina: \n"))
            nome = input("\n\tDigite o nome da disciplina: \n")
            dicionario= {
                "codigo": codigo,
                "nome": nome
            }
     
            dados = recuperar_arquivo()
            dados.append(dicionario)
            salvar_arquivo(dados)
            print("\n\tDisciplina incluído com sucesso.")
            input("\n\tAperte <ENTER> ")

        def listar ():

            '''
            Lista todas as disciplinas no sistema.
            1 - Exibe uma mensagem de cabeçalho
            2 - Percorre a lista de disciplinas
            3 - Exibe os dados da disciplina

            '''
            print (" ---Opção selecionada -> LISTAR Disciplinas: ---")
            dados = recuperar_arquivo()
            if len(dados) < 1:
                print("\n\tAinda não existe DISCIPLINAS CADASTRADAS\n")
                input('Aperte <ENTER> ')
            else:
                print("\n\t--- LISTA DE DISCIPLINAS ---\n")
                print("\n\tCódigo\tNome")
                for disciplina in dados:
                    print(str(disciplina['codigo']) + "\t" + disciplina['nome'])
                input("\naperte ENTER> ")

        def atualizar ():
            '''
            Atualiza os dados de uma disciplina no sistema.
            1 - Solicita ao usuário o código da disciplina
            2 - Verifica se o professor existe
            3 - Edita dicionário
            4 - Salva dados atualizados no arquivo
            '''
            print("\n\t--- opção selecionada -> ATUALIZAÇÃO de disciplina ---\n")
            dados = recuperar_arquivo ()
            codigo = int(input("\n\tDigite o código da disicplina a ser atualizado: \n"))
            contem = False
            for iteravel in dados:
                if iteravel['codigo'] == codigo:
                    codigo = int(input("Informe o novo código da disciplina: "))
                    nome = input("Informe o novo nome da disciplina: ")
                    iteravel['codigo'] = codigo
                    iteravel['nome'] = nome
                    contem = True
                    break
                
            if not contem:
                print("\n Sem registros de Disciplina. ")
            else:
                salvar_arquivo(dados)
            input("\naperte <ENTER> ")

        def excluir ():
            '''
            Exclui uma disciplina do sistema.
            1 - Solicita ao usuário o código da disciplina
            2 - Procura na lista e deleta caso ache
            3 - Caso tenha percorrido a lista e não encontrado, mostra mensagem
            4 - Salva dados atualizados no arquivo

            '''
            print("\n\t--- opção selecionada -> EXCLUSÃO de disciplina ---\n")
            dados = recuperar_arquivo ()
            codigo = int(input("\n\tDigite o código da disciplina a ser excluído: \n"))
            contem = False
            for iteravel in dados:
                if iteravel['codigo'] == codigo:
                    dados.remove(dados)
                    contem = True
                    break

            if not contem:
                print("\nRegistro não encontrado.")
            else:
                salvar_arquivo(dados)
   
            print("\n\tDsciplina excluída com sucesso.")
            input("\nAperte <ENTER> ")

        def recuperar_arquivo():
            '''
            Polimosfismo da função para disciplinas
            '''
            try:
                with open('Disciplinas.json', 'r') as file:
                    dados = json.load(file)
            except FileNotFoundError:
                dados = []
            return dados
       
        def salvar_arquivo (dados):
            '''
                Salva dados de disciplinas
            '''
            with open('Disciplinas.json', 'w') as file:  
                json.dump(dados, file)  


    elif opcao == 4:
        opcao_1 = "Turmas"
        """
        polimorfismos das funções para turma
        """
        def incluir ():
            '''
            Inclui uma nova turma no sistema.
            1 - Solicita dados da turma
            2 - Cria um dicionário da turma
            3 - Salva a disciplina no arquivo
            4 - Exibe uma mensagem de sucesso
            '''
            print (" ---Opção selecionada -> INCLUSÃO de turmas: ---")
            codigo_turma = int(input("\n\tDigite o código da turma: \n"))
            codigo_professor = int(input("\n\tDigite o código do professor: \n"))
            codigo_disciplina = int(input("\n\tDigite o código da disciplina: \n"))

            dicionario = {
                "codigo_turma": codigo_turma,
                "codigo_professor": codigo_professor,
                "codigo_disciplina": codigo_disciplina
                }
            
            dados = recuperar_arquivo()
            dados.append(dicionario)
            salvar_arquivo(dados)
            
            print("\n\tTurma incluída com sucesso.")
            input("\nPressione ENTER para continuar.")

        def listar ():
            '''
            Lista todas as turmas no sistema.
            1 - Exibe uma mensagem de cabeçalho
            2 - Percorre a lista de disciplinas
            3 - Exibe a lista de disciplinas
            '''
            print("\n\tOpção selecionada -> listagem de turmas: \n")
            dados = recuperar_arquivo()
            print("Código da turma\tCódigo do professor\tCódigo da disciplina")
            if len(turma) < 1:
                print("\n\tAinda não existe TURMAS CADASTRADAS\n")
                input('pressione ENTER para continuar')
            else:
                print("\n\t--- LISTA DE TURMAS ---\n")
                print("Código da turma\tCódigo do professor\tCódigo da disciplina")
                for turma in dados:
                    print(str(turma['codigo_turma']) + "\t" + str(turma['codigo_professor']) + "\t" + str(turma['codigo_disciplina']))
            input("\nAperte <ENTER> ")

        def atualizar ():
            '''
            Atualiza os dados de uma turma no sistema.
            1 - Solicita ao usuário o código da turma
            2 - Verifica se o professor existe
            3 - Edita dicionário
            4 - Salva dados atualizados no arquivo
            '''
            print (" opção selecionada -> ATUALIZAÇÃO de turmas: ")
            dados = recuperar_arquivo ()
            codigo_turma = int(input("\n\tDigite o código da turma a ser atualizada: \n"))
            contem = False
            for iteravel in dados:
                if iteravel['codigo_turma'] == codigo_turma:
                    codigo_turma = int(input("Informe o novo código da turma: "))
                    codigo_professor = int(input("Informe o novo professor da turma: "))
                    codigo_disciplina = int(input("Informe o novo código da disciplina"))
                    iteravel['codigo_turma'] = codigo_turma
                    iteravel['codigo_professor'] = codigo_professor
                    iteravel['codigo_disciplina'] = codigo_disciplina
                    contem = True
                    break
                
            if not contem:
                print("\nTurma não encontrada.")
            else:
                salvar_arquivo(dados)
            input("\nAperte <ENTER> ")

        def excluir_turma ():
            '''
            Exclui uma turma do sistema.
            1 - Solicita ao usuário o código da turma
            2 - Procura na lista e deleta caso ache
            3 - Caso tenha percorrido a lista e não encontrado, mostra mensagem
            4 - Salva dados atualizados no arquivo
            '''
            print("\n\t--- opção selecionada -> EXCLUSÃO de turma ---\n")
            dados = recuperar_arquivo ()
            codigo_turma = int(input("\n\tDigite o código da turma a ser excluído: \n"))
            contem = False
            for iteravel in dados:
                if iteravel['codigo_turma'] == codigo_turma:
                    dados.remove(iteravel)
                    contem = True
                    break
            if not contem:
                print("\nRegistro não encontrado.")
            else:
                salvar_arquivo(dados)
            print("\n\tTurma excluída com sucesso.")
            input("\nAperte <ENTER> ")

        def recuperar_arquivo():
            '''
            polimorfismo de recuperação para 'Turmas.json'
            '''
            try:
                with open('Turmas.json', 'r') as file:
                    dados = json.load(file)
            except FileNotFoundError:
                dados = []
            return dados

        def salvar_arquivo(dados):
            with open('Turmas.json', 'w') as file: 
                json.dump(dados, file)  

    elif opcao == 5:
        '''
        Polimorfismos para as funções de Matriculas
        '''
        opcao_1 = "Matriculas"

        def incluir ():
            '''
            Inclui uma nova matrícula no sistema.
            1 - Solicita ao usuário os dados da matrícula
            2 - Cria um dicionário com os dados da turma
            3 - Salva a disciplina no arquivo
            4 - Exibe uma mensagem de sucesso
            '''
            print (" --- opção selecionada -> INCLUSÃO de matriculas: ---")
            dados = recuperar_arquivo()
            codigo_turma = int(input("\n\tDigite o código da turma: \n"))
            codigo = int(input("\n\tDigite o código do aluno: \n"))
            dicionario = {
                "codigo_turma": codigo_turma,
                "codigo": codigo,
                }
    
            dados = recuperar_arquivo()
            dados.append(dicionario)
            salvar_arquivo(dados)
            print("\n\tMatricula incluída com sucesso.")
            input("\nAperte <ENTER> ")

        def listar ():
            '''
            Lista todas as matrículas no sistema.
            1 - Percorre a lista de disciplinas
            2 - Exibe os dados da disciplina
            '''
            print("\n\t --- Opção selecionada -> LISTAR matriculas: ---\n")
            dados = recuperar_arquivo()
            if len(dados) < 1:
                print("\n\tAinda não existe matriculas cadastradas\n")
                input('pressione <ENTER> ')
            else:
                print("\n\t--- LISTA DE MATRICULAS ---\n")
                print("Código da turma\tCódigo do Estudante")
                for matricula in dados:
                    print(str(matricula['codigo_turma']) + "\t" + str(matricula['codigo']))
            input("\nAperte <ENTER> ")

        def atualizar ():
            '''
            Atualiza os dados de uma matrícula no sistema.
            1 Solicita ao usuário o código da turma
            2 - Verifica se o matricula existe
            3 - Edita dicionário
            4 - Salva dados atualizados no arquivo
            '''
            print("Opção selecionada -> atualização de matriculas: ")
            dados = recuperar_arquivo ()
            codigo_turma = int(input("\n\tDigite o código da turma a ser atualizada: \n"))
            contem = False
            for iteravel in dados:
                if iteravel['codigo_turma'] == codigo_turma:
                    codigo_turma = int(input("Informe o novo código da turma: "))
                    codigo = int(input("Informe o novo código do aluno: "))
                    iteravel['codigo_turma'] = codigo_turma
                    iteravel['codigo'] = codigo
                    contem = True
                    break
            if not contem:
                print("\nRegistro não encontrado.")
            else:
                salvar_arquivo(dados)
            input("\nPressione <ENTER> ")

        def excluir ():
            '''
            Exclui uma matrícula do sistema.
            1 - Solicita ao usuário o código da turma
            2 - Procura na lista e deleta caso ache
            3 - Caso tenha percorrido a lista e não encontrado, mostra mensagem
            4 - Salva dados atualizados no arquivo
            '''
            print("\n\t--- opção selecionada: Exclusção de matriculas ---\n")
            dados = recuperar_arquivo ()
            codigo_turma = int(input("\n\tDigite o código da turma a ser excluído: \n"))
            contem = False
            for iteravel in dados:
                if iteravel['codigo_turma'] == codigo_turma:
                    dados.remove(iteravel)
                    contem = True
                    break
            if not contem:
                print("\nRegistro não encontrado.")
            else:
                salvar_arquivo(dados)
            print("\n\tTurma excluída com sucesso.")
            input("\nPressione <ENTER> .")

        def recuperar_arquivo():
            '''
            polimorfismo para arquivo Matriculas.json
            '''
            try:
                with open('Matriculas.json', 'r') as file:
                    dados = json.load(file)
            except FileNotFoundError:
                dados = []
            return dados

        def salvarArquivo(dados):
            with open('Matriculas.json', 'w') as file: 
                json.dump(dados, file)  


    elif opcao == 9:
        print ("Opção de saída selecionada: ")
        break

    else:
        print ("Opção selecionada inválida, tente novamente: ")
        input (" aperte <ENTER> ")
        continue

    ## Acesso ao menu secundário

    opcao_2 = 1
    while opcao_2 !=9:
        opcao_2 = menu_secundario(opcao_1)
        if opcao_2 ==1:
            # método incluir
            incluir()
        elif opcao_2 ==2:
            # método listar
            listar()
        elif opcao_2 ==3:
            # método atualizar
            atualizar()
        elif opcao_2 ==4:
            # método excluir
            excluir() 
        elif opcao_2 ==9:
            # opção de sair do método
            print ("opção de saída: ")
            continue
        else:
            print("opção inválida, selecione opção contida no menu secundário: ")
            input(" aperte <ENTER> ")
        
print("--------------------------------------------------\n")
print("\n\t--- Finalizando o programa ---\n")

## detalhes da versão anterior 
'''
Funções utilizadas na versão anterior:

# funções da area do professor

def incluir_professor ():
    '''
    #Inclui um novo professor no sistema.
'''
    # Solicita ao usuário os dados do professor
    codigo = int(input("\n\tDigite o código do professor: \n"))
    nome = str(input("\n\tDigite o nome do professor: \n"))
    cpf = str(input("\n\tDigite o CPF do professor: \n"))

    # Cria um dicionário com os dados do professor
    professor = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf
    }

    # Salva o professor no arquivo

    dados = recuperar_arquivo()
    dados.append(professor)
    salvar_arquivo(dados)
    print("\n\tPROFESSOR incluído com sucesso.")
    input("\nPressione ENTER para continuar.")

def listar_professor ():

    '''
    #Lista todos os professores no sistema.
'''

    dados = recuperar_arquivo()
    if len(professor) < 1:
        print("\n\tAinda não existe PROFESSORES CADASTRADOS\n")
        input('pressione ENTER para continuar')
    else:
            # Percorre estudantes e imprime
        print("Código\tNome\tCPF")
    for professor in dados:
        print(str(professor['codigo']) + "\t" + professor['nome'] + "\t" + professor['cpf'])
                    
        input("\nPressione ENTER para continuar.")

def atualizar_professor ():

    '''
    #Atualiza os dados de um professor no sistema.
'''

    # Solicita ao usuário o código do professor
    codigo = int(input("\n\tDigite o código do professor a ser atualizado: \n"))
    print("\n\t--- opção selecionada: ATUALIZAÇÃO de Professor ---\n")
    dados = recuperar_arquivo ()
    # Verifica se o professor existe
    contem = False
    for professor in dados:
        if professor['codigo'] == codigo:
         
    
            codigo = int(input("Informe o novo código do estudante: "))
            nome = input("Informe o novo nome do estudante: ")
            cpf = input("Informe o novo CPF do estudante: ")

            # Edita dicionário
            professor['codigo'] = codigo
            professor['nome'] = nome
            professor['cpf'] = cpf
                        
            contem = True
            break
        
    if not contem:
        print("\nRegistro não encontrado.")
    else:
        # Salva dados atualizados no arquivo
        salvar_arquivo(dados)

    input("\nPressione ENTER para continuar.")

def excluir_professor ():

    '''
    #Exclui um professor do sistema.
'''

    # Solicita ao usuário o código do professor
    print("\n\t--- opção selecionada: EXCLUSÃO de Professor ---\n")
    dados = recuperar_arquivo ()
    codigo = int(input("\n\tDigite o código do professor a ser excluído: \n"))

    # Procura na lista e deleta caso ache
    contem = False
    for professor in dados:
        if professor['codigo'] == codigo:
            dados.remove(professor)
            contem = True
            break

    # Caso tenha percorrido a lista e não encontrado, mostra mensagem
    if not contem:
        print("\nRegistro não encontrado.")
    else:
        # Salva dados atualizados no arquivo
        salvar_arquivo(dados)
            
    print("\n\tProfessor excluído com sucesso.")
    input("\nPressione ENTER para continuar.")


# funções da area de disciplinas

def incluir_disciplina ():

    '''
    #Inclui uma nova disciplina no sistema.
'''

    # Solicita ao usuário os dados da disciplina
    codigo = int(input("\n\tDigite o código da disciplina: \n"))
    nome = str(input("\n\tDigite o nome da disciplina: \n"))

    # Cria um dicionário com os dados da disciplina
    disciplina = {
        "codigo": codigo,
        "nome": nome
    }

    # Salva a disciplina no arquivo
    dados = recuperar_arquivo()
    dados.append(disciplina)
    salvar_arquivo(dados)

    # Exibe uma mensagem de sucesso
  
    print("\n\tDisciplina incluído com sucesso.")

    input("\nPressione ENTER para continuar.")

def listar_disciplina ():

    '''
    #Lista todas as disciplinas no sistema.
'''

    # Exibe uma mensagem de cabeçalho
    dados = recuperar_arquivo()

    if len(disciplina) < 1:
        print("\n\tAinda não existe DISCIPLINAS CADASTRADAS\n")
        input('pressione ENTER para continuar')
    else:
        print("\n\t--- LISTA DE DISCIPLINAS ---\n")
        print("\n\tCódigo\tNome")

    # Percorre a lista de disciplinas
    for disciplina in dados:
        # Exibe os dados da disciplina
        print(str(disciplina['codigo']) + "\t" + disciplina['nome'])
    
    input("\nPressione ENTER para continuar.")

def atualizar_disciplina ():

    '''
    #Atualiza os dados de uma disciplina no sistema.
'''

    # Solicita ao usuário o código da disciplina
    codigo = int(input("\n\tDigite o código da disicplina a ser atualizado: \n"))
    print("\n\t--- opção selecionada: ATUALIZAÇÃO de disciplina ---\n")
    dados = recuperar_arquivo ()

        # Verifica se o professor existe
    contem = False
    for disciplina in dados:
        if disciplina['codigo'] == codigo:
         
    
            codigo = int(input("Informe o novo código da disciplina: "))
            nome = input("Informe o novo nome da disciplina: ")
            

            # Edita dicionário
            disciplina['codigo'] = codigo
            disciplina['nome'] = nome
            
                        
            contem = True
            break
        
    if not contem:
        print("\nRegistro não encontrado.")
    else:
        # Salva dados atualizados no arquivo
        salvar_arquivo(dados)

    input("\nPressione ENTER para continuar.")

def excluir_disciplina ():

    '''
    #Exclui uma disciplina do sistema.
'''

    # Solicita ao usuário o código da disciplina
    print("\n\t--- opção selecionada: EXCLUSÃO de disciplina ---\n")
    dados = recuperar_arquivo ()
    codigo = int(input("\n\tDigite o código da disciplina a ser excluído: \n"))

    # Procura na lista e deleta caso ache
    contem = False
    for disciplina in dados:
        if disciplina['codigo'] == codigo:
            dados.remove(disciplina)
            contem = True
            break

    # Caso tenha percorrido a lista e não encontrado, mostra mensagem
    if not contem:
        print("\nRegistro não encontrado.")
    else:
        # Salva dados atualizados no arquivo
        salvar_arquivo(dados)
            
    print("\n\tDsciplina excluída com sucesso.")
    input("\nPressione ENTER para continuar.")

# funções para turmas

def incluir_turma ():

    '''
    #Inclui uma nova turma no sistema.
'''

    # Solicita ao usuário os dados da turma
    codigo_turma = int(input("\n\tDigite o código da turma: \n"))
    codigo_professor = int(input("\n\tDigite o código do professor: \n"))
    codigo_disciplina = int(input("\n\tDigite o código da disciplina: \n"))

    # Cria um dicionário com os dados da turma
    turma = {
        "codigo_turma": codigo_turma,
        "codigo_professor": codigo_professor,
        "codigo_disciplina": codigo_disciplina
        }
    

    # Salva a disciplina no arquivo
    dados = recuperar_arquivo()
    dados.append(turma)
    salvar_arquivo(dados)

    # Exibe uma mensagem de sucesso
    print("\n\tTurma incluída com sucesso.")

    input("\nPressione ENTER para continuar.")

def listar_turma ():

    '''
    #Lista todas as turmas no sistema.
'''

    # Exibe uma mensagem de cabeçalho
    print("\n\t--- LISTA DE TURMAS ---\n")
    print("Código da turma\tCódigo do professor\tCódigo da disciplina")
    dados = recuperar_arquivo()

    if len(turma) < 1:
        print("\n\tAinda não existe TURMAS CADASTRADAS\n")
        input('pressione ENTER para continuar')
    else:
        print("\n\t--- LISTA DE TURMAS ---\n")
        print("Código da turma\tCódigo do professor\tCódigo da disciplina")

    # Percorre a lista de disciplinas
    for turma in dados:
        # Exibe os dados da disciplina
        print(str(turma['codigo_turma']) + "\t" + str(turma['codigo_professor']) + "\t" + str(turma['codigo_disciplina']))
    
    input("\nPressione ENTER para continuar.")

def atualizar_turma ():

    '''
    #Atualiza os dados de uma turma no sistema.
'''

    # Solicita ao usuário o código da turma
    codigo_turma = int(input("\n\tDigite o código da turma a ser atualizada: \n"))
    dados = recuperar_arquivo ()

            # Verifica se o professor existe
    contem = False
    for turma in dados:
        if turma['codigo_turma'] == codigo_turma:
         
    
            codigo_turma = int(input("Informe o novo código da turma: "))
            codigo_professor = int(input("Informe o novo professor da turma: "))
            codigo_disciplina = int(input("Informe o novo código da disciplina"))
            

            # Edita dicionário
            turma['codigo_turma'] = codigo_turma
            turma['codigo_professor'] = codigo_professor
            turma['codigo_disciplina'] = codigo_disciplina
                        
            contem = True
            break
        
    if not contem:
        print("\nRegistro não encontrado.")
    else:
        # Salva dados atualizados no arquivo
        salvar_arquivo(dados)

    input("\nPressione ENTER para continuar.")

def excluir_turma ():

    '''
    #Exclui uma turma do sistema.
'''

    # Solicita ao usuário o código da turma
    print("\n\t--- opção selecionada: EXCLUSÃO de turma ---\n")
    dados = recuperar_arquivo ()
    codigo_turma = int(input("\n\tDigite o código da turma a ser excluído: \n"))

    # Procura na lista e deleta caso ache
    contem = False
    for turma in dados:
        if turma['codigo_turma'] == codigo_turma:
            dados.remove(turma)
            contem = True
            break

    # Caso tenha percorrido a lista e não encontrado, mostra mensagem
    if not contem:
        print("\nRegistro não encontrado.")
    else:
        # Salva dados atualizados no arquivo
        salvar_arquivo(dados)
            
    print("\n\tTurma excluída com sucesso.")
    input("\nPressione ENTER para continuar.")

# funções de matriculas

def incluir_matricula ():

    '''
    #Inclui uma nova matrícula no sistema.
'''

    # Solicita ao usuário os dados da matrícula
    dados = recuperar_arquivo()
    codigo_turma = int(input("\n\tDigite o código da turma: \n"))
    codigo = int(input("\n\tDigite o código do aluno: \n"))

    # Verifica se a turma e o estudante existem
    turma = None
    for turma in dados:
        if turma['codigo_turma'] == codigo_turma:
            break

    estudante = None
    for estudante in dados:
        if estudante['codigo'] == codigo:
            break

    # Se a turma ou o estudante não existirem, exibe uma mensagem de erro
    if turma is None or estudante is None:
        print("\n\tTurma ou estudante não encontrado.")
        return

    # Verifica se a matrícula já existe
    matricula_existente = False
    for matricula in dados:
        if matricula['codigo_turma'] == codigo_turma and matricula['codigo_estudante'] == codigo:
            matricula_existente = True
            break

    # Se a matrícula já existir, exibe uma mensagem de erro
    if matricula_existente:
        print("\n\tMatrícula já existente.")
        return



    # Cria um dicionário com os dados da turma
    matricula = {
        "codigo_turma": codigo_turma,
        "codigo": codigo,
        }
    



    # Salva a disciplina no arquivo
    dados = recuperar_arquivo()
    dados.append(matricula)
    salvar_arquivo(dados)

    # Exibe uma mensagem de sucesso
    print("\n\tMatricula incluída com sucesso.")
    input("\nPressione ENTER para continuar.")

def listar_matricula ():

    '''
    #Lista todas as matrículas no sistema.
'''

    # Exibe uma mensagem de cabeçalho

    print("\n\t--- LISTA DE MATRICULAS ---\n")
    print("Código da turma\tCódigo do Estudante")


    if len(matricula) < 1:
        print("\n\tAinda não existe TURMAS CADASTRADAS\n")
        input('pressione ENTER para continuar')
    else:
        print("\n\t--- LISTA DE MATRICULAS ---\n")
        print("Código da turma\tCódigo do Estudante")

    # Percorre a lista de disciplinas
    for matricula in dados:
        # Exibe os dados da disciplina
        print(str(matricula['codigo_turma']) + "\t" + str(matricula['codigo']))
    
    dados = recuperar_arquivo()
    print("\n\t--- LISTA DE MATRÍCULAS ---\n")
    print("Código da turma\tCódigo do estudante")
    input("\nPressione ENTER para continuar.")

def atualizar_matrícula ():

    '''
    #Atualiza os dados de uma matrícula no sistema.
'''

    # Solicita ao usuário o código da turma
    dados = recuperar_arquivo ()
    codigo_turma = int(input("\n\tDigite o código da turma a ser atualizada: \n"))


    # Verifica se o matricula existe
    contem = False
    for matricula in dados:
        if matricula['codigo_turma'] == codigo_turma:
         
    
            codigo_turma = int(input("Informe o novo código da turma: "))
            codigo = int(input("Informe o novo código do aluno: "))

             # Edita dicionário
            matricula['codigo_turma'] = codigo_turma
            matricula['codigo'] = codigo

                        
            contem = True
            break
        
    if not contem:
        print("\nRegistro não encontrado.")
    else:
        # Salva dados atualizados no arquivo
        salvar_arquivo(dados)

    input("\nPressione ENTER para continuar.")

def excluir_matrícula ():

    '''
    #Exclui uma matrícula do sistema.
'''

    # Solicita ao usuário o código da turma
    print("\n\t--- opção selecionada: EXCLUSÃO de turma ---\n")
    dados = recuperar_arquivo ()
    codigo_turma = int(input("\n\tDigite o código da turma a ser excluído: \n"))

    # Procura na lista e deleta caso ache
    contem = False
    for matricula in dados:
        if matricula['codigo_turma'] == codigo_turma:
            dados.remove(matricula)
            contem = True
            break

    # Caso tenha percorrido a lista e não encontrado, mostra mensagem
    if not contem:
        print("\nRegistro não encontrado.")
    else:
        # Salva dados atualizados no arquivo
        salvar_arquivo(dados)
            
    print("\n\tTurma excluída com sucesso.")
    input("\nPressione ENTER para continuar.")

'''
