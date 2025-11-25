# Programa para ler três números e mostrar o menor

# Entrada de dados
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Verificando o menor número
menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Saída de dados
print(f"O menor número é: {menor}")