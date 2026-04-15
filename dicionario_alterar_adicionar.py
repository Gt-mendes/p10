# Dicionario original
pessoa = {"nome": "Joao", "idade": 25, "cidade": "Sao Paulo"}
print(f"Original: {pessoa}")

# ALTERAR: muda o valor da chave "idade"
pessoa["idade"] = 26
print(f"Apos alterar idade: {pessoa}")

# ADICIONAR: cria uma nova chave "profissao"
pessoa["profissao"] = "Engenheiro"
print(f"Apos adicionar profissao: {pessoa}")