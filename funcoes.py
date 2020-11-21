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