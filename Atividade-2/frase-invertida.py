def inverter_palavras_da_frase(frase):
    """
    Recebe uma frase, inverte cada palavra e retorna a nova frase.
    """

    #   Quebra a frase em uma lista de palavras
    palavras = frase.split(' ')

    #  Cria uma lista vazia para guardar as palavras invertidas
    palavras_invertidas = []

    #   Itera (passa) por cada palavra da lista
    for palavra in palavras:
        #  Inverte a palavra atual usando [::-1] e a adiciona na nova lista
        palavra_invertida = palavra[::-1]
        palavras_invertidas.append(palavra_invertida)

    #  Junta as palavras invertidas de volta em uma única string,
    #    usando um espaço (" ") como separador.
    nova_frase = " ".join(palavras_invertidas)

    return nova_frase


# --- Testando a função ---
minha_frase = "O Thiago é muito legal"
frase_resultado = inverter_palavras_da_frase(minha_frase)

print(f"Frase original:  {minha_frase}")
print(f"Frase invertida: {frase_resultado}")

# Teste 2
minha_frase_2 = "O teste funcionou"
print(f"\nFrase original:  {minha_frase_2}")
print(f"Frase invertida: {inverter_palavras_da_frase(minha_frase_2)}")