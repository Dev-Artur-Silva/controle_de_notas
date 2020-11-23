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
        0 - Sair
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
            funcoes.menu_um(excel_professores, excel_alunos)
            funcoes.salvar_dados(excel_disciplinas, excel_notas, excel_professores, excel_alunos)

        elif (menu == 2):
            #Cadastro de Alunos (Nome, matrícula, data de nascimento)
            funcoes.menu_dois(excel_professores, excel_alunos)
            funcoes.salvar_dados(excel_disciplinas, excel_notas, excel_professores, excel_alunos)

        elif (menu == 3):
            #Cadastro de Disciplinas (Código, nome, matrícula do professor)
            funcoes.menu_tres(excel_disciplinas, excel_professores)
            funcoes.salvar_dados(excel_disciplinas, excel_notas, excel_professores, excel_alunos)

        elif (menu == 4):
            #Cadastro de Notas (Código da Disciplina, matrícula do aluno, Nota 1, Nota2)
            funcoes.menu_quatro(excel_disciplinas, excel_alunos, excel_notas)
            funcoes.salvar_dados(excel_disciplinas, excel_notas, excel_professores, excel_alunos)

        elif (menu == 5):
                #o Imprimir a disciplina, professor da disciplina, relação dos alunos e
                #suas notas finais (média da Nota 1 e Nota 2).
            funcoes.relatorio_notas(excel_disciplinas, excel_notas, excel_professores, excel_alunos)
            
        elif (menu == 0):
            break

menu()