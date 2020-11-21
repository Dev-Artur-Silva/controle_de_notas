import pandas as pd
import funcoes

arquivo = pd.ExcelFile("C:aps_excel.xlsx")
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
            nome = input('Digite o nome do Professor: ')
            matricula = int(input('Digite a matricula do Professor'))
            data = input('Digite a data de nascimento (dd/mm/aaaa): ')
            
            funcoes.cadastrar_professor(excel_professores, nome, matricula, data)

        elif (menu == 2):
            #Cadastro de Alunos (Nome, matrícula, data de nascimento)
            nome = input('Digite o nome do Aluno: ')
            matricula = int(input('Digite a matricula do Aluno'))
            data = input('Digite a data de nascimento (dd/mm/aaaa): ')

            funcoes.cadastrar_aluno(excel_alunos, nome, matricula, data)
        
        elif (menu == 3):
            #Cadastro de Disciplinas (Código, nome, matrícula do professor)
            codigo = int(input('Digite o codigo da disciplina: '))
            nome = input('Digite o nome da disciplina: ')
            matricula = int(input('Digite a matricula do Professor: '))

            funcoes.cadastrar_disciplina(excel_disciplinas, codigo, nome, matricula)
        
        elif (menu == 4):
            #Cadastro de Notas (Código da Disciplina, matrícula do aluno, Nota 1, Nota2)
            codigo = int(input('Digite o codigo da disciplina: '))
            matricula = input('Digite a matricula do Professor: ')
            nota1 = float(input('Digite a 1ª nota do aluno: '))
            nota2 = float(input('Digite a 2ª nota do aluno: '))
            
            funcoes.cadastrar_notas(excel_notas, codigo, matricula, nota1, nota2)


        elif (menu == 5):
                #o Imprimir a disciplina, professor da disciplina, relação dos alunos e
                #suas notas finais (média da Nota 1 e Nota 2).
            pass
menu()