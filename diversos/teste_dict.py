"""Contar caracteres
"""

def contar_caracteres(s):
    """[summary]
     Args:
        s ([strig]): [string a ser contada]
    
    >>> contar_caracteres('joao')
    {'a':1, 'j':1, 'o':2}

    """
    resultado={}
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado
      

if __name__ == "__main__":
    print(contar_caracteres('joao'))