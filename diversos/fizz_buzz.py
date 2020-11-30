"""

    Se o numero for divisivel por 2 fizz
    se por 5 buzz 
    senao o proprio numero

    1 até o parametro

>>> 
 
"""
def fizz_buzz(n):
    for num in range(1, n+1, 1):
        if (num % 2 == 0) and (num % 5 == 0):
            print(f'{num}: Fizz buzz')
        elif num % 5 ==0:
            print(f'{num}: buzz')
        elif num % 2 == 0:
            print(f'{num}: Fizz')
        else:
            print(f'{num}')

    # while cont <= n:
    #     if n % 2 == 0:
    #         print("Fizz")
    #     elif n % 5 == 0:
    #         print("Buzz")
    #     else:
    #         print(f'{n}')
    #     cont += 1


if __name__ == "__main__":
    fizz_buzz(10)