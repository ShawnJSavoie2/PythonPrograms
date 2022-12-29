# Python 3.9.0

# BaseNRadixToBaseNCommon

def BaseNRadixToBaseNCommon(Radix, FromBase, ToBase):


    '''
    Parameters:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    FromBase: must be a string integer that's one number between and including 2 and 16.
    ToBase: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    Radix
    BaseNRadixToBaseTenRadix
    RadixToCommon
    FormatNumber
    '''


    Radix = I.Radix(Radix)
    Separators = [',', '_']
    WorkingRadix = ''
    for Element in Radix:
        if Element in Separators:
            continue
        else:
            WorkingRadix = f'{WorkingRadix}{Element}'
    Radix = WorkingRadix
    if FromBase != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, FromBase)
    if ToBase != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, ToBase)
    Common = I.RadixToCommon(Radix, ToBase)
    Common = I.FormatNumber(Common)
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base N Radix To Base N Common')
        print()
        Radix = input('Enter Radix: ')
        FromBase = input('Enter FromBase: ')
        ToBase = input('Enter ToBase: ')
        Common = I.BaseNRadixToBaseNCommon(Radix, FromBase, ToBase)
        print()
        Print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        
