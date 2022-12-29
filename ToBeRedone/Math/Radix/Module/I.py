
# Python 3.9.0

# Radix

def Radix(Radix):


    '''
    Parameters:
    Radix: must be a string radix ('n', 'n.n')
    '''


    if '.' not in Radix:
        Radix = f'{Radix}.0'
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Radix')
        print()
        Radix = input('Enter Radix: ')
        Radix = I.Radix(Radix)
        print()
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break


# Python 3.9.0

# Radix

def Radix(Radix):


    '''
    Parameters:
    Radix: must be a string radix ('n', 'n.n')
    '''


    if '.' not in Radix:
        Radix = f'{Radix}.0'
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Radix')
        print()
        Radix = input('Enter Radix: ')
        Radix = I.Radix(Radix)
        print()
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
