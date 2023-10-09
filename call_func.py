def meny1(stack_nr):
    print(f'Meny1 Börjar------{stack_nr}')
    while True:
        val = input('>>>')
        if val == 'q':
            break
        else:
            meny2(stack_nr + 1)    

    print('Meny1 Slutar-----')


def meny2(stack_nr):
    print(f'Meny2 Börjar------nr {stack_nr}')
    while True:
        val = input('>>>')
        if val == 'q':
            break
        else:
            meny1(stack_nr + 1)

    print('Meny2 Slutar-----')

meny1(0)