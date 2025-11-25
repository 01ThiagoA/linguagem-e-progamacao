import math

def eh_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

print("--- Verificando números primos de 1 a 100 ---")
for numero in range(1, 101):
    print(f"{numero} -> {'VERDADEIRO (é primo)' if eh_primo(numero) else 'FALSO (não é primo)'}")