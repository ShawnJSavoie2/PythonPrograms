# Python 3.9.0

# GetPower

def GetPower(Root, Exponent):


    '''
    Parameters:
    Root: must be a literal integer or float.
    Exponent: must be a literal integer.
    '''


    Power = Root
    for Times in range(Exponent - 1):
        Power *= Root
    return Power


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Get Power')
        print()
        Root = float(input('Enter Root: '))
        Exponent = int(input('Enter Exponent: '))
        Power = I.GetPower(Root, Exponent)
        print()
        print(Power)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
