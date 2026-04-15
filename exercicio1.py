# Exercicio 1: Lista de compras
compras = ["Arroz", "Feijao", "Macarrao", "Leite", "Cafe"]
print(f"Lista inicial: {compras}")

compras.append("Açúcar")
compras.append("Sal")
compras.append("Oleo")
print(f"Itens adicionados: {compras[5]}, {compras[6]}, {compras[7]}")


compras.pop(0)
print(f"Lista final: {compras}")