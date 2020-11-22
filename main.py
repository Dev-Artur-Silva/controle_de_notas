import pandas as pd
import funcoes

arquivo = pd.ExcelFile("C:dados.xlsx")
excel_professores = pd.read_excel(arquivo, 'Professores')
excel_alunos = pd.read_excel(arquivo, 'Alunos')
excel_notas = pd.read_excel(arquivo, 'Notas')
excel_disciplinas = pd.read_excel(arquivo, 'Disciplinas')

def menu():

    while True:
        print('''
        Escolha uma opção do menu:

        1 - Cadastro de Professores
        2 - Cadastro de Alunos
        3 - Cadastro de Disciplinas
        4 - Cadastro de Notas
        5 - Relatorio de Notas (por disciplina)
        ''')

        try:
            menu = int(input('O que deseja? '))
            print()
            assert 0 <= menu <= 5
        except AssertionError:
            print('Valor fora do limite.')
            continue
        except ValueError:
            print('Somente numeros.')
            continue
        
        if (menu == 1):
            #Cadastro de Professores (Nome, matrícula, data de nascimento)
            nome = input('Digite o nome do Professor: ').capitalize()
            while True:

                while True:
                    try:
                        matricula = int(input('Digite a matricula do Professor(0 para sair): '))

                        if matricula == 0:
                            break

                        elif matricula in excel_professores.values or matricula in excel_alunos.values:
                            print('Matricula ja cadastrada.')
                            continue
                        break
                    except ValueError:
                        print('Apenas numeros.')

                if matricula == 0:
                    break

                while True:
                    data = input('Digite a data de nascimento (dd/mm/aaaa): ')
                    if len(data) != 10:
                        print('Digite no formato dd/mm/aaaa')
                        continue
                    break
                
                funcoes.cadastrar_professor(excel_professores, nome, matricula, data)
                break
        elif (menu == 2):
            #Cadastro de Alunos (Nome, matrícula, data de nascimento)
            nome = input('Digite o nome do Aluno: ').capitalize()
            while True:

                while True:
                    try:
                        matricula = int(input('Digite a matricula do Aluno(0 para sair): '))
                        
                        if matricula == 0:
                            break

                        elif matricula in excel_professores.values or matricula in excel_alunos.values:
                                print('Matricula ja cadastrada.')
                                continue
                        break
                    except ValueError:
                        print('Apenas numeros.')
                
                if matricula == 0:
                            break

                while True:
                    data = input('Digite a data de nascimento (dd/mm/aaaa): ')
                    if len(data) != 10:
                        print('Digite no formato dd/mm/aaaa')
                        continue
                    break

                funcoes.cadastrar_aluno(excel_alunos, nome, matricula, data)
                break
        elif (menu == 3):
            #Cadastro de Disciplinas (Código, nome, matrícula do professor)
            while True:

                while True:
                    try:
                        codigo = int(input('Digite o codigo da disciplina(0 para sair): '))
                        if codigo == 0:
                            break
                        if codigo in excel_disciplinas.values:
                            print('Disciplina ja cadastrada.')
                            continue
                        break
                    except ValueError:
                        print('Apenas numeros.')
                
                if codigo == 0:
                    break

                nome = input('Digite o nome da disciplina: ').capitalize()

                while True:
                    try:
                        matricula = int(input('Digite a matricula do Professor(0 para sair): '))

                        if matricula == 0:
                            break
                        if matricula not in excel_professores.values:
                            print('Professor nao cadastrado.')
                            continue
                        break
                    except ValueError:
                        print('Apenas numeros.')

                if matricula == 0:
                        break

                funcoes.cadastrar_disciplina(excel_disciplinas, codigo, nome, matricula)
                break
        elif (menu == 4):
            #Cadastro de Notas (Código da Disciplina, matrícula do aluno, Nota 1, Nota2)
            while True:

                while True:
                    try:
                        codigo = int(input('Digite o codigo da disciplina(0 para sair): '))
                        if codigo == 0:
                            break

                        elif codigo not in excel_disciplinas.values:
                            print('Disciplina nao cadastrada.')
                            continue
                        break
                    except ValueError:
                        print('Apenas numeros.')

                if codigo == 0:
                            break

                while True:    
                    try:
                        matricula = int(input('Digite a matricula do Aluno: '))
                        if matricula == 0:
                            break
                        
                        elif matricula not in excel_alunos.values:
                            print('Aluno nao cadastrado.')
                            continue

                        for posicao_notas, linha_notas in excel_notas.iterrows():
                            if codigo == linha_notas['Codigo da Disciplina'] and matricula == linha_notas['Matricula do Aluno']:
                                print('Aluno ja cadastrado nesta disciplina.')
                                continue
                        break
                    except ValueError:
                        print('Apenas numeros.')

                if matricula == 0:
                            break

                while True:

                    try:
                        nota1 = float(input('Digite a 1ª nota do aluno: '))
                        nota2 = float(input('Digite a 2ª nota do aluno: '))
                        break
                    except ValueError:
                        print('Digite um valor valido.')
                        
                funcoes.cadastrar_notas(excel_notas, codigo, matricula, nota1, nota2)
                break
        elif (menu == 5):
                #o Imprimir a disciplina, professor da disciplina, relação dos alunos e
                #suas notas finais (média da Nota 1 e Nota 2).
            funcoes.relatorio_notas(excel_disciplinas, excel_notas, excel_professores, excel_alunos)
menu()