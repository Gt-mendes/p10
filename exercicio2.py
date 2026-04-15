# Exercicio 2: Maior, menor e soma
numeros = [15, 8, 30, 5, 12, 25]
print("=" * 40)
print(f"Lista: {numeros}")
print("=" * 40)
numeros.sort()
print(f"Lista ordenada: {numeros}")
print("=" * 40)

maior = max(numeros)
print(f"Maior valor: {maior}")

menor = min(numeros)
print(f"Menor valor: {menor}")

soma = sum(numeros)
print(f"Soma: {soma}")