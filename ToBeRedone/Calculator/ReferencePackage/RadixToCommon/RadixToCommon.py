# Python 3.9.0

# RadixToCommon

def RadixToCommon(Radix, Base):


    '''
    Parameters:
    Radix: must be a string radix with a base that's between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseNRadixToBaseTenRadix,
    RoundUpOrTruncate
    BaseTenIntegerToBaseNInteger
    SimplifyCommon
    '''


    if Base != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, Base)
    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[IndexOfPoint:]
    Denominator = 2
    GoodToGo = 'No'
    while GoodToGo == 'No':
        Numerator = float(Fraction) * Denominator
        if Numerator % 1 == 0:
            GoodToGo = 'Yes'
        else:
            Numerator = I.RoundUpOrTruncate(Numerator)
            if Numerator % 1 == 0:
                GoodToGo = 'Yes'
            else:
                Denominator += 1
    if Base != '10':
        Whole = I.BaseTenIntegerToBaseNInteger(Whole, Base)
        Numerator = I.BaseTenIntegerToBaseNInteger(str(int(Numerator)), Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(str(Denominator), Base)
    Whole = int(Whole)
    Numerator = int(Numerator)
    Denominator = int(Denominator)
    if Numerator == 0:
        Denominator = 0
        Common = f'{Whole}:{Numerator}|{Denominator}'
    else:
        Common = f'{Whole}:{Numerator}|{Denominator}'
        Common = I.SimplifyCommon(Common, Base)
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('RadixToCommon')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        print()
        Common = I.RadixToCommon(Radix, Base)
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
