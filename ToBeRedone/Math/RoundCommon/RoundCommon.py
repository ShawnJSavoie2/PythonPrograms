# Python 3.9.0

# RoundCommon

def RoundCommon(Common, Base, RootDenominator, PowerDenominator):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    RootDenominator: must be a string integer.
    PowerDenominator: must be a string integer.

    Dependencies:
    Programmer's:
    CommonToRadix
    BaseNRadixToBaseTenRadix
    GetExponent
    SimplifyRoundedCommon
    '''


    Radix = I.CommonToRadix(Common, Base)
    WorkingRootDenominator = ''
    for Element in RootDenominator:
        if Element != ',':
            WorkingRootDenominator = f'{WorkingRootDenominator}{Element}'
    RootDenominator = WorkingRootDenominator
    WorkingPowerDenominator = ''
    for Element in PowerDenominator:
        if Element != ',':
            WorkingPowerDenominator = f'{WorkingPowerDenominator}{Element}'
    PowerDenominator = WorkingPowerDenominator
    if Base != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, Base)
        RootDenominator = I.BaseNIntegerToBaseTenInteger(RootDenominator, Base)
        PowerDenominator = I.BaseNIntegerToBaseTenInteger(PowerDenominator, Base)
    RootDenominator = int(RootDenominator)
    PowerDenominator = int(PowerDenominator)
    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[IndexOfPoint:]
    Exponent = I.GetExponent(RootDenominator, PowerDenominator)
    Denominators = [RootDenominator]
    WorkingPowerDenominator = RootDenominator
    for Times in range(Exponent - 1):
        WorkingPowerDenominator *= RootDenominator
        Denominators.append(WorkingPowerDenominator)
    Denominator = PowerDenominator
    Numerator = float(Fraction) * Denominator
    if Numerator % 1 == 0:
        if Numerator in Denominators:
            Denominator /= Numerator
            Numerator /= Numerator
    else:
        Numerator = round(Numerator)
        if Numerator in Denominators:
            Denominator /= Numerator
            Numerator /= Numerator
    if Base != '10':
        Whole = I.BaseTenIntegerToBaseNInteger(Whole, Base)
        Numerator = I.BaseTenIntegerToBaseNInteger(Numerator, Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(Denominator, Base)
    else:
        Numerator = int(Numerator)
        Denominator = int(Denominator)
    Common = f'{Whole}:{Numerator}|{Denominator}'
    Common = I.SimplifyRoundedCommon(Common, Base, str(RootDenominator))
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Round Common')
        print()
        Common = input('Enter Common: ')
        Base = input('Enter Base: ')
        RootDenominator = input('Enter RootDenominator: ')
        PowerDenominator = input('Enter PowerDenominator: ')
        Common = I.RoundCommon(Common, Base, RootDenominator, PowerDenominator)
        print()
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        
