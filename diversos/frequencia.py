def frequencia(s):
    caracteres = sorted(s)
    resultado = {}

    for caracter in caracteres:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == "__main__":
    print(frequencia('joao'))
    print(frequencia('joao'))
