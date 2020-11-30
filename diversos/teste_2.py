"""

implementar strstr() -
dadas duas strings agulha e palheiro, a função retorna o 1o indice da ocorrência da agulha no palheiro ou -1 se não encontrar
Ex: strstr(‘palheiro’, ‘agulha no palheiro’) retorna 10

# >>> str1 = 'palheiro'
# >>> str2 = 'agulha no palheiro azul'


"""

def strstr(str1, str2):
    for index, letra in enumerate(str2):
        if letra == str1[0]:
            if str1 == str2[index:index+len(str1)]:
                return index
            else:
                return -1


if __name__ == '__main__':
    print(strstr('palheiro', 'agulha no palheiro azul'))
