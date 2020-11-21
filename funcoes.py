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
            
            for posicao_notas, linha_notas in excel_notas.iterrows():

                for posicao_alunos, linha_alunos in excel_alunos.iterrows():

                    if linha_disciplina['Matricula do Professor'] == linha_professor['Matricula']:

                        print('Disciplina:', linha_disciplina['Nome'],', Nome do Professor:',linha_professor['Nome'])

                        if linha_disciplina['Codigo'] == linha_notas['Codigo da Disciplina']:

                            if linha_notas['Matricula do Aluno'] == linha_alunos['Matricula']:

                                nota_final = (linha_notas['Nota 1'] + linha_notas['Nota 2']) / 2

                                print('Nome do Aluno:',linha_alunos['Nome'],', Nota final:',nota_final)