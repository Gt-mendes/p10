# Dicionario da pessoa
pessoa = {
    "nome": "Joao",
    "idade": 25,
    "cidade": "Sao Paulo",
    "profissao": "Engenheiro"
}

print("Informacoes da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")