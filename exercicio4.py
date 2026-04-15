# Exercicio 4: Dicionario do meu pet
meu_pet = {
    "Nome": "Amora",
    "Tipo": "Cachorro",
    "Idade": 7,
    "Cor": "Branca e preta",
    "Raça": "Lhasa Apso"
}

print("Informacoes do meu pet:")
for chave, valor in meu_pet.items():
    print(f"{chave}: {valor}")