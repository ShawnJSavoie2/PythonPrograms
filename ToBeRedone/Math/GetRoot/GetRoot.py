# Python 3.9.0

# GetRoot

def GetRoot(Power, Exponent):


    '''
    Parameters:
    Power: must be a literal float.
    Exponent: must be a literal integer.

    Dependencies:
    Programmer's:
    RoundUpOrTruncate
    '''


    Quantity = 1.0
    PreviousWorkingRoot = 0
    WorkingRoot = 1.0
    WorkingPower = 1.0
    Root = 0
    while WorkingPower != Power:
        for Times in range(Exponent - 1):
            WorkingPower *= WorkingRoot
        WorkingPower = I.RoundUpOrTruncate(WorkingPower)
        if WorkingPower == Power:
            Root = WorkingRoot
        elif WorkingPower < Power:
            PreviousWorkingRoot = WorkingRoot
            WorkingRoot += Quantity
            WorkingPower = WorkingRoot
        else:
            Quantity /= 10.0
            WorkingRoot = (PreviousWorkingRoot + Quantity)
            WorkingPower = WorkingRoot
    return Root


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Get Root')
        print()
        Power = float(input('Enter Power: '))
        Exponent = int(input('Enter Exponent: '))
        Root = I.GetRoot(Power, Exponent)
        print()
        print(Root)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        
