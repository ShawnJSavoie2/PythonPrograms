# Python 3.9.0

# BaseNCommonToBaseNCommon

def BaseNCommonToBaseNCommon(Common, FromBase, ToBase):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    FromBase: must be a string integer that's one number between and including 2 and 16.
    ToBase: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    Common
    CommonToRadix
    BaseNRadixToBaseTenRadix
    RadixToCommon
    FormatNumber
    '''


    Common = I.Common(Common)
    Separators = [',', '_']
    WorkingCommon = ''
    for Element in Common:
        if Element in Separators:
            continue
        else:
            WorkingCommon = f'{WorkingCommon}{Element}'
    Common = WorkingCommon
    Radix = I.CommonToRadix(Common, FromBase)
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
        print('Base N Common To Base N Common')
        print()
        Common = input('Enter Common: ')
        FromBase = input('Enter FromBase: ')
        ToBase = input('Enter ToBase: ')
        Common = I.BaseNCommonToBaseNCommon(Common, FromBase, ToBase)
        print()
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        
