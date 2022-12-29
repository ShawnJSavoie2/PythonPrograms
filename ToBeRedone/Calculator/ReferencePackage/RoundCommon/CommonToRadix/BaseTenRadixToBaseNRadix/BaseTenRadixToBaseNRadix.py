# Python 3.9.0

# BaseTenRadixToBaseNRadix

def BaseTenRadixToBaseNRadix(Radix, Base):


    '''
    Parameters:
    Radix: must be a string radix that's in base 10.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    GetExponent
    SimplifyRoundedCommon
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    Whole = int(Whole)
    Base = int(Base)
    if Whole != 0:
        Exponent = 1
        Magnitude = Base ** Exponent
        while Whole > Magnitude:
            Exponent = Exponent + 1
            Magnitude = Base ** Exponent
        if Magnitude > Whole:
            Magnitude = Magnitude / Base
            Exponent = Exponent - 1
        Digits = []
        Digit = Whole // Magnitude
        Remainder = Whole - (Digit * Magnitude)
        Digits.append(int(Digit))
        if Exponent != 0:
            Magnitude = Magnitude / Base
            Exponent = Exponent - 1
            if Remainder >= Base:
                GoodToGo = 'no'
                while GoodToGo == 'no':
                    if Magnitude > Remainder:
                        Digits.append(0)
                        Magnitude = Magnitude / Base
                        Exponent = Exponent - 1
                    else: # Magnitude < Remainder
                        Digit = Remainder // Magnitude
                        Remainder = Remainder - (Digit * Magnitude)
                        Digits.append(int(Digit))
                        Magnitude = Magnitude / Base
                        Exponent = Exponent - 1
                    if Remainder >= Base:
                        GoodToGo = 'no'
                    else:
                        GoodToGo = 'yes'
            if Exponent != 0:
                for Count in range(Exponent):
                    Digits.append(0)
            Digits.append(int(Remainder))
        AlternativeDigits = {
            '10': 'A',
            '11': 'B',
            '12': 'C',
            '13': 'D',
            '14': 'E',
            '15': 'F'
            }
        Whole = ''
        for Digit in Digits:
            if str(Digit) in AlternativeDigits:
                Whole = f'{Whole}{AlternativeDigits[str(Digit)]}'
            else:
                Whole = f'{Whole}{Digit}'
    #Fraction part
    if Fraction != '0':
        RootDenominator = int(Base)
        PowerDenominator = int(Base) ** 16
        Exponent = I.GetExponent(RootDenominator, PowerDenominator)
        Denominators = [RootDenominator]
        WorkingPowerDenominator = RootDenominator
        for Times in range(Exponent - 1):
            WorkingPowerDenominator *= RootDenominator
            Denominators.append(WorkingPowerDenominator)
        Denominator = PowerDenominator
        Numerator = float(f'.{Fraction}') * Denominator
        if Numerator % 1 == 0:
            if Numerator in Denominators:
                Denominator /= Numerator
                Numerator /= Numerator
        else:
            Numerator = round(Numerator)
            if Numerator in Denominators:
                Denominator /= Numerator
                Numerator /= Numerator
        Numerator = int(Numerator)
        Denominator = int(Denominator)
        Common = f'0:{Numerator}|{Denominator}'
        Common = I.SimplifyRoundedCommon(Common, '10', Base)
        IndexOfColon = Common.index(':')
        IndexOfBar = Common.index('|')
        Numerator = Common[(IndexOfColon + 1):IndexOfBar]
        Denominator = Common[(IndexOfBar + 1):]
        Numerator = I.BaseTenIntegerToBaseNInteger(Numerator, Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(Denominator, Base)
        Fraction = Numerator
        for Times in range((len(Denominator) - 1 - len(Numerator))):
            Fraction = f'0{Fraction}'
    Radix = f'{Whole}.{Fraction}'
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base Ten Radix To Base N Radix')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        print()
        Radix = I.BaseTenRadixToBaseNRadix(Radix, Base)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
