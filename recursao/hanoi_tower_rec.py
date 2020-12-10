'''
Recursive exercise
Hanoi Tower
Take the pieces from tower A to tower C using an Auxiliar tower B
The biggest piece can´t stay on another ones smaller

'''

def hanoi(n, orig='A', aux='B', dest='C'):
    if n >= 1:
        hanoi(n-1, orig, dest, aux)
        print('{}->  {}: {}'.format(orig, dest, n))
        hanoi(n-1, aux, orig, dest)

for i in range(1, 4):
    print('##### hanoi %s', i)
    hanoi(i)
