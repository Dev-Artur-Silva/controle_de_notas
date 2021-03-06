import pandas as pd

def cadastrar_professor(excel_professores, nome, matricula, data):
    linha = [nome, matricula, data]
    excel_professores.loc[len(excel_professores)] = linha

def cadastrar_aluno(excel_alunos, nome, matricula, data):
    linha = [nome, matricula, data]
    excel_alunos.loc[len(excel_alunos)] = linha

def cadastrar_disciplina(excel_disciplinas, codigo, nome, matricula_professor):
    linha = [codigo, nome, matricula_professor]
    excel_disciplinas.loc[len(excel_disciplinas)] = linha

def cadastrar_notas(excel_notas, codigo, matricula_aluno, nota1, nota2):
    linha = [codigo, matricula_aluno, nota1, nota2]
    excel_notas.loc[len(excel_notas)] = linha

def relatorio_notas(excel_disciplinas, excel_notas, excel_professores, excel_alunos):
    #Imprimir a disciplina, professor da disciplina, relação dos alunos e
    #suas notas finais (média da Nota 1 e Nota 2).
    for posicao_disciplina, linha_disciplina in excel_disciplinas.iterrows():
        print()
        for posicao_professor, linha_professor in excel_professores.iterrows():

            if linha_disciplina['Matricula do Professor'] == linha_professor['Matricula']:

                print('Disciplina:', linha_disciplina['Nome'],', Nome do Professor:',linha_professor['Nome'])
            
                for posicao_notas, linha_notas in excel_notas.iterrows():

                    for posicao_alunos, linha_alunos in excel_alunos.iterrows():

                        if linha_disciplina['Codigo'] == linha_notas['Codigo da Disciplina']:

                            if linha_notas['Matricula do Aluno'] == linha_alunos['Matricula']:

                                nota_final = (linha_notas['Nota 1'] + linha_notas['Nota 2']) / 2

                                print('Nome do Aluno:',linha_alunos['Nome'],', Nota final:',nota_final)

def menu_um(excel_professores, excel_alunos):

    nome = input('Digite o nome do Professor: ').capitalize()
    while True:
        while True:
            try:
                var = False
                matricula = int(input('Digite a matricula do Professor(0 para sair): '))
                if matricula == 0:
                    break

                for posicao_professor, linha_professor in excel_professores.iterrows():
                    if matricula == linha_professor['Matricula']:
                        print('Matricula ja cadastrada')
                        var = True
                        continue

                for posicao_alunos, linha_alunos in excel_alunos.iterrows():
                    if matricula == linha_alunos['Matricula']:
                        print('Matricula ja cadastrada.')
                        var = True
                        continue

                if var == True:
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

            elif data[2] != '/' and data[5] != '/':
                print('Digite no formato dd/mm/aaaa')
                continue

            break
        
        cadastrar_professor(excel_professores, nome, matricula, data)
        print('\nProfessor cadastrado!\n')
        break

def menu_dois(excel_professores, excel_alunos):

    while True:
        nome = input('Digite o nome do Aluno: ').capitalize()
        while True:
            try:
                var = False
                matricula = int(input('Digite a matricula do Aluno(0 para sair): '))
                
                if matricula == 0:
                    break

                for posicao_professor, linha_professor in excel_professores.iterrows():
                    if matricula == linha_professor['Matricula']:
                        print('Matricula ja cadastrada')
                        var = True
                    
                for posicao_alunos, linha_alunos in excel_alunos.iterrows():
                    if matricula == linha_alunos['Matricula']:
                        print('Matricula ja cadastrada.')
                        var = True
                
                if var == True:
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
            
            elif data[2] != '/' and data[5] != '/':
                print('Digite no formato dd/mm/aaaa')
                continue

            break

        cadastrar_aluno(excel_alunos, nome, matricula, data)
        print('\nAluno cadastrado!\n')
        break

def menu_tres(excel_disciplinas, excel_professores):
    while True:

        while True:
            try:
                var = False
                codigo = int(input('Digite o codigo da disciplina(0 para sair): '))
                if codigo == 0:
                    break

                for posicao_disciplina, linha_disciplina in excel_disciplinas.iterrows():
                    if codigo == linha_disciplina['Codigo']:
                        print('Codigo ja cadastrado.')
                        var = True
                        break
                
                if var == True:
                    continue

                break

            except ValueError:
                print('Apenas numeros.')
        
        if codigo == 0:
            break

        nome = input('Digite o nome da disciplina: ').capitalize()

        while True:
            try:
                var = True
                matricula = int(input('Digite a matricula do Professor(0 para sair): '))
                if matricula == 0:
                    break

                for posicao_professor, linha_professor in excel_professores.iterrows():
                    if matricula == linha_professor['Matricula']:
                        var = False
                
                for posicao_disciplina, linha_disciplina in excel_disciplinas.iterrows():
                    if matricula == linha_disciplina['Matricula do Professor']:
                        var = True
                        break
                
                if var == True:
                    print('Nao ha professor com essa matricula ou Professor ja cadastrado como professor de uma disciplina.')
                    continue

                break

            except ValueError:
                print('Apenas numeros.')

        if matricula == 0:
            break

        cadastrar_disciplina(excel_disciplinas, codigo, nome, matricula)
        print("\nDisciplina cadastrada!\n")
        break

def menu_quatro(excel_disciplinas, excel_alunos, excel_notas):
    while True:

        while True:
            try:
                var = True
                codigo = int(input('Digite o codigo da disciplina(0 para sair): '))
                if codigo == 0:
                    break
                
                for posicao_disciplina, linha_disciplina in excel_disciplinas.iterrows():
                    if linha_disciplina['Codigo'] == codigo:
                        var = False
                        break
                
                if var == True:
                    print('Disciplina ainda nao cadastrada.')
                    continue
                break

            except ValueError:
                print('Apenas numeros.')

        if codigo == 0:
            break

        while True:    
            try:
                var = False
                matricula = int(input('Digite a matricula do Aluno(0 para sair): '))

                if matricula == 0:
                    break
                
                for posicao_alunos, linha_alunos in excel_alunos.iterrows():
                    if matricula == linha_alunos['Matricula']:
                        var = False
                        break
                    else:
                        var = True

                for posicao_notas, linha_notas in excel_notas.iterrows():
                    if codigo == linha_notas['Codigo da Disciplina'] and matricula == linha_notas['Matricula do Aluno']:
                        var = True

                if var == True:
                    print('Aluno nao cadastrado ou Aluno ja cadastrado nesta disciplina.')
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
                
        cadastrar_notas(excel_notas, codigo, matricula, nota1, nota2)
        print('\nNotas cadastradas!\n')
        break

def salvar_dados(excel_disciplinas, excel_notas, excel_professores, excel_alunos):
    # Criar objeto para leitura e selecionar planilha
    # Criar objeto para escrita
    excel_writer = pd.ExcelWriter("dados.xlsx")
    excel_professores.to_excel(excel_writer, 'Professores', index=False)
    excel_alunos.to_excel(excel_writer, 'Alunos', index=False)
    excel_disciplinas.to_excel(excel_writer, 'Disciplinas', index=False)
    excel_notas.to_excel(excel_writer, 'Notas', index=False)
    # Salvar e fechar arquivo
    excel_writer.save()