# Enunciado: Corrija a função para adicionar ou atualizar a nota de um aluno.
# Se o aluno não existir no dicionário, ele deve ser criado.

alunos = {"João": 8.5, "Maria": 9.0}
 
def atualizar_nota(nome, nota):
    if nome in alunos:
        alunos[nome] = nota
        print(f"Nota de {nome} atualizada para {nota}")
    else:
        alunos[nome] = nota
        print(f"Aluno {nome} adicionado junto a {nota}")
 
atualizar_nota("João", 7.0)
atualizar_nota("Pedro", 7.5)
print(alunos)