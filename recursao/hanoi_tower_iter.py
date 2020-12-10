'''
Recursive exercise
Hanoi Tower
Take the pieces from tower A to tower C using an Auxiliar tower B
The biggest piece can´t stay on another ones smaller

'''


def hanoi(n, orig='A', aux='B', dest='C'):

    stack = [(False, n, orig, aux, dest)]

    while stack:
        print_flag, n, orig, aux, dest = stack.pop()
        if n < 1:
            continue
        if not print_flag:
            stack.append((True, n, orig, aux, dest))
            stack.append((False, n - 1, orig, dest, aux))
        else:
            print('{}->  {}: {}'.format(orig, dest, n))
            stack.append((False, n - 1, aux, orig, dest))


for i in range(1, 4):
    print('##### hanoi %s', i)
    hanoi(i)
