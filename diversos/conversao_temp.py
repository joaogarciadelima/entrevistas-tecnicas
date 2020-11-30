"""conversão temperatura"""



def conversao(temp_fahrenheint):
    """[summary]

    Args:
        temp_fahrenheint ([type]): [description]

        return celsius

        formula de conversão:
        C = 5 * ((F-32) / 9).
    """
    celsius = 5 * ((temp_fahrenheint - 32)/9)

    return celsius

if __name__ == "__main__":
    print(conversao(35))
