# Dicionario completo
pessoa = {
    "nome": "Joao",
    "idade": 25,
    "cidade": "Sao Paulo",
    "profissao": "Engenheiro",
    "telefone": "99999-9999"
}
print(f"Original: {pessoa}")

# METODO 1: del - remove a chave (nao retorna o valor)
del pessoa["profissao"]
print(f"Apos del pessoa[profissao]: {pessoa}")

# METODO 2: pop() - remove a chave e RETORNA o valor
telefone_removido = pessoa.pop("telefone")
print(f"Apos pop(telefone): {pessoa}")
print(f"Telefone removido: {telefone_removido}")

# METODO 3: popitem() - remove e retorna o ULTIMO par
chave_removida, valor_removido = pessoa.popitem()
print(f"Apos popitem(): {pessoa}")
print(f"Ultimo par removido: {chave_removida}:{valor_removido}")