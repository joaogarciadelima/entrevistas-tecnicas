
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
>>> retorna_segundo_maior([5, 5, 5, 2, 2, 4, 4, 4, 6, 6, 6])
5
>>> retorna_segundo_maior([5, 4])
4
'''

def retorna_segundo_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort()
    return lista_unica[-2] if len(lista_unica) > 1 else lista_unica[0]
