"""Contar caracteres
"""

def contar_caracteres(s):
    """[summary]
     Args:
        s ([strig]): [string a ser contada]
    
    >>> contar_caracteres('joao')
    a:1
    j:1
    o:2
    """
    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1
    for caracter in caracteres_ordenados[1:]:
        if caracter_anterior == caracter:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}:{contagem}')
        

if __name__ == "__main__":
    print(contar_caracteres('joao'))