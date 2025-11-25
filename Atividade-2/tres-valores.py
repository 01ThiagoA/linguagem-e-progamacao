import math

# Entrada de dados
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Verificando se formam um triângulo
if a < b + c and b < a + c and c < a + b:
    print("Os valores formam um triângulo.")
    
    # Cálculo da área (Fórmula de Heron)
    p = (a + b + c) / 2  # semiperímetro
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    print(f"A área do triângulo é: {area:.2f}")
else:
    print("Os valores não formam um triângulo.")
    print(f"Valores informados: a={a}, b={b}, c={c}")