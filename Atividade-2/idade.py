# Programa para converter idade em dias para anos, meses e dias

# Entrada de dados
dias = int(input("Digite sua idade em dias: "))

# Cálculos
anos = dias // 365
meses = (dias % 365) // 30
dias_restantes = (dias % 365) % 30

# Saída de dados
print(f"Sua idade é {anos} anos, {meses} meses e {dias_restantes} dias.")