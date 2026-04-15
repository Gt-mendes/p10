# Lista original com 5 alunos
alunos = ["Ana", "Bruno", "Carla", "Daniel", "Elisa"]
print(f"Original: {alunos}")

# METODO 1: remove() - remove pelo VALOR (primeira ocorrencia)
alunos.remove("Carla")
print(f"Apos remove(Carla): {alunos}")

# METODO 2: pop() - remove pelo INDICE e RETORNA o valor removido
removido = alunos.pop(2)
print(f"Apos pop(2): {alunos}")
print(f"Elemento removido: {removido}")

# METODO 3: del - remove pelo INDICE (nao retorna o valor)
del alunos[0]
print(f"Apos del alunos[0]: {alunos}")