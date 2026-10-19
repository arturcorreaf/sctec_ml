import numpy as np 

notas = np.array([[8.5, 9.0, 7.5],
                  [6.0, 7.5, 5.0],
                  [9.5, 8.0, 9.0],
                  [5.0, 6.0, 4.5]])
alunos = np.array(["Ana","Bruno","Carla","Diego"])

media_aluno = notas.mean(axis=1).round(2)
media_prova = notas.mean(axis=0).round(2)
situacao = np.where(media_aluno >= 7, "Aprovado", "Reprovado")
melhor = np.argmax(media_aluno)

print("\n====== Boletim dos alunos ====== \n")
for nome, media, sit in zip(alunos, media_aluno, situacao):
    print(nome, "|", media, "|", sit)

print("\nMelhor aluno: " + str(alunos[melhor]) + "\nMédia: " + str(media_aluno[melhor]))

print("\nMédia de cada aluno:")
print(media_aluno)
print("\nMédia de cada prova:")
print(media_prova)




