
''''
>>> retorna_segundo_maior([1,2,3])
2
>>> retorna_segundo_maior([1,1,2,3,3,4])
3
>>> retorna_segundo_maior([1,1, 2, 2, 3, 3, 4, 4, 5, 5])
4
>>> retorna_segundo_maior([5, 5, 4, 4, 3, 3, 2, 2, 1, 1])
4
>>> retorna_segundo_maior([5, 5, 4, 4])
4
>>> retorna_segundo_maior([5, 5, 3, 3, 4, 4])
4
>>> retorna_segundo_maior([5, 5, 2, 2, 4, 4, 6, 6])
5
>>> retorna_segundo_maior([5, 5,])
5
'''

def retorna_segundo_maior(lista):
    """
    Recebe uma lista e deve retornar o maior número e o segundo maior número
    """
    maior_num = segundo_maior = lista[0]

    for num in lista:
        if num < maior_num:
            segundo_maior = num
            break

    for num in lista:
        if num != maior_num and num > segundo_maior:
            segundo_maior = num
        if num > maior_num:
            segundo_maior = maior_num
            maior_num = num

    return segundo_maior
