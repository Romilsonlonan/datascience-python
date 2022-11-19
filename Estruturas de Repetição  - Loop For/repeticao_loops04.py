"""
Exercício Resolvido de Laço Aninhado

Você foi contratado por uma escola para fazer o seguinte script em Python:
Primeiro, pergunta a quem vai usar o script quantos alunos tem na sala.
Depois, quantas matérias cada aluno estuda.

Em seguida o usuário vai preenchendo a nota de cada matéria, de cada aluno.
Seu programa deve fornecer a média de cada aluno e a média geral da turma.

Solução:

Vamos armazenar o número de alunos na variável alunos e o número de matérias 
em materias.

O primeiro laço é o que vai percorrer os alunos:
Aluno 1, depois aluno 2, o aluno 3...ou seja: range(alunos)

Depois, para cada aluno vamos dar as respectivas notas de cada matéria.A cada 
nota que o usuário der, vamos somar ela na variável 'mediaAluno', e ao final 
basta dividirmos esse número pelo número de matérias e temos a média daquele 
aluno. A cada iteração do primeiro FOR, antes de digitarmos as notas de cada 
matéria, devemos zerar essa variável!

Quando tivermos a 'mediaAluno', vamos somar esse valor na variável 'mediaTurma', 
e no final do programa dividimos essa variável pelo número de alunos, para ter a 
média geral da turma.

Veja como ficou o código final:
"""


alunos=int(input("Quantos alunos tem na turma: ") )
materias=int(input("Quantas matérias eles estudam: ") )

mediaTurma=0
for aluno in range(alunos):
    print("Aluno",aluno+1,":")
    
    mediaAluno=0
    for materia in range(materias):
          print("Nota da materia",materia+1,":", end='')
          nota=int(input())
          mediaAluno += nota

    mediaAluno /= materias
    print("Media desse aluno:",mediaAluno,"\n")
    
    mediaTurma += mediaAluno

mediaTurma /= alunos
print("Media da turma:",mediaTurma)