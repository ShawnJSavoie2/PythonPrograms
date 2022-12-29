
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
        Common = I.RadixToCommon(Radix, Base)
        print()
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        


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
        Common = I.RadixToCommon(Radix, Base)
        print()
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        

# Python 3.9.0

# BaseNRadixToBaseTenRadix

def BaseNRadixToBaseTenRadix(Radix, Base):


    '''
    Parameters:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseNIntegerToBaseTenInteger
    '''


    AlternativeDigits = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
        }
    RadixList = []
    for Element in Radix:
        if Element in AlternativeDigits:
            RadixList.append(AlternativeDigits[Element])
        else:
            RadixList.append(Element)
    IndexOfPoint = RadixList.index('.')
    Whole = RadixList[:IndexOfPoint]
    Fraction = RadixList[(IndexOfPoint + 1):]
    # Whole part.
    PositiveMagnitudes = []
    for Exponent in range(len(Whole)):
        Magnitude = int(Base) ** Exponent
        PositiveMagnitudes.append(Magnitude)
    PositiveMagnitudes.reverse()
    WorkingWhole = 0
    for Index in range(len(PositiveMagnitudes)):
        WorkingWhole += (float(Whole[Index]) * PositiveMagnitudes[Index])
    Whole = int(WorkingWhole)
    # Fraction part
    Denominator = '1'
    for Times in range(len(Fraction)):
        Denominator = f'{Denominator}0'
    Numerator = I.BaseNIntegerToBaseTenInteger(Fraction, Base)
    Denominator = I.BaseNIntegerToBaseTenInteger(Denominator, Base)
    Fraction = str(int(Numerator) / int(Denominator))
    Fraction = Fraction[2:]
    # Whole and Fraction parts
    Radix = f'{Whole}.{Fraction}'
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base N Radix To Base Ten Radix')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        Radix = I.BaseNRadixToBaseTenRadix(Radix, Base)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        

# Python 3.9.0

# BaseNIntegerToBaseTenInteger

def BaseNIntegerToBaseTenInteger(Integer, Base):


    '''
    Parameters:
    Integer: must be a string integer that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    '''


    AlternativeDigits = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
        }
    IntegerList = []
    for Element in Integer:
        if Element in AlternativeDigits:
            IntegerList.append(AlternativeDigits[Element])
        else:
            IntegerList.append(Element)
    PositiveMagnitudes = []
    for Exponent in range(len(IntegerList)):
        Magnitude = int(Base) ** Exponent
        PositiveMagnitudes.append(Magnitude)
    PositiveMagnitudes.reverse()
    Integer = 0
    for Index in range(len(PositiveMagnitudes)):
        Integer += (int(IntegerList[Index]) * PositiveMagnitudes[Index])
    return str(Integer)


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print('\nBase N Integer To Base Ten Integer\n')
        Integer = input('Enter Integer: ')
        Base = input('Enter Base: ')
        Integer = I.BaseNIntegerToBaseTenInteger(Integer, Base)
        print()
        print(Integer)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
        

# Python 3.9.0

# BaseTenIntegerToBaseNInteger

def BaseTenIntegerToBaseNInteger(Integer, Base):


    '''
    Parameters:
    Integer: must be a string integer that's in base 10.
    Base: must be a string integer that's one number between and including 2 and 16.
    '''


    Integer = int(Integer)
    Base = int(Base)
    Exponent = 1
    Magnitude = Base ** Exponent
    while Integer > Magnitude:
        Exponent = Exponent + 1
        Magnitude = Base ** Exponent
    if Magnitude > Integer:
        Magnitude = Magnitude / Base
        Exponent = Exponent - 1
    Digits = []
    Digit = int(Integer // Magnitude)
    Remainder = Integer - (Digit * Magnitude)
    Digits.append(Digit)
    if Exponent != 0:
        Magnitude = Magnitude / Base
        Exponent = Exponent - 1
        if Remainder >= Base:
            GoodToGo = 'No'
            while GoodToGo == 'No':
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
                    GoodToGo = 'No'
                else:
                    GoodToGo = 'Yes'
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
    Integer = ''
    for Digit in Digits:
        if str(Digit) in AlternativeDigits:
            Integer = f'{Integer}{AlternativeDigits[Digit]}'
        else:
            Integer = f'{Integer}{Digit}'
    return Integer


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base Ten Integer To Base N Integer')
        print()
        Integer = input('Enter Integer: ')
        Base = input('Enter Base: ')
        Integer = I.BaseTenIntegerToBaseNInteger(Integer, Base)
        print()
        print(Integer)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# RoundUpOrTruncate

def RoundUpOrTruncate(Radix):


    '''
    Parameters:
    Radix: must be a literal float.

    Dependencies:
    Programmer's:
    EFormatToRadix
    '''


    Radix = str(Radix)
    if 'e' in Radix:
        Radix = I.EFormatToRadix(Radix, Base)
    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    LengthOfFraction = len(Fraction)
    Count = 0
    for Digit in Fraction:
        if Digit == '0':
            Count += 1
        else:
            break
    if Count >= 4:
        if Count == LengthOfFraction or Count == (LengthOfFraction - 1):
            Radix = float(Whole)
            return Radix
    else:
        Count = 0
    for Element in Fraction:
        if Element == '9':
            Count += 1
        else:
            break
    if Count >= 4:
        if Count == LengthOfFraction or Count == (LengthOfFraction - 1):
            Radix = float(Whole) + 1
            return Radix
    return float(Radix)


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Round Up Or Truncate')
        print()
        Radix = input('Enter Radix: ')
        Radix = I.RoundUpOrTruncate(Radix)
        print()
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
        

# Python 3.9.0

# EFormatToRadix

def EFormatToRadix(EFormat, Base):


    '''
    Parameters:
    EFormat: must be a string EFormat ('ne[+/-]n') that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Modules:
    Programmer's:
    BaseNIntegerToBaseTenInteger
    '''


    IndexOfE = EFormat.index('e')
    Radix = EFormat[:IndexOfE]
    Sign = EFormat[(IndexOfE + 1)]
    Exponent = EFormat[(IndexOfE + 2):]
    if '.' in Radix:
        Radix = f'{Radix[0]}{Radix[2:]}'
    if Base != '10':
        Exponent = I.BaseNIntegerToBaseTenInteger(Exponent, Base)
    if Sign == '+':
        Zeros = int(Exponent) - (len(Radix) - 1)
        for Zero in range(Zeros):
            Radix = f'{Radix}0'
        Radix = f'{Radix}.0'
    else: # Sign == '-'
        for Zero in range(int(Exponent) - 1):
            Radix = f'0{Radix}'
        Radix = f'0.{Radix}'
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('EFormatToRadix')
        print()
        EFormat = input('Enter EFormat: ')
        Base = input('Enter Base: ')
        Radix = I.EFormatToRadix(EFormat, Base)
        print()
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        

# Python 3.9.0

# SimplifyCommon

def SimplifyCommon(Common, Base):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') with a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseNIntegerToBaseTenInteger
    BaseTenIntegerToBaseNInteger
    '''


    IndexOfColon = Common.index(':')
    Whole = Common[:IndexOfColon]
    Fraction = Common[(IndexOfColon + 1):]
    IndexOfBar = Fraction.index('|')
    Numerator = Fraction[:IndexOfBar]
    Denominator = Fraction[(IndexOfBar + 1):]
    if Base != '10':
        Whole = I.BaseNIntegerToBaseTenInteger(Whole, Base)
        Numerator = I.BaseNIntegerToBaseTenInteger(Numerator, Base)
        Denominator = I.BaseNIntegerToBaseTenInteger(Denominator, Base)
    Whole = int(Whole)
    Numerator = int(Numerator)
    Denominator = int(Denominator)
    Divisor = 2
    GoodToGo = 'No'
    while GoodToGo == 'No':
        if Divisor <= Numerator:
            if Numerator % Divisor == 0 and Denominator % Divisor == 0:
                Numerator /= Divisor
                Denominator /= Divisor
            else:
                Divisor += 1
        else:
            GoodToGo = 'Yes'
    if Base != '10':
        Whole = I.BaseTenIntegerToBaseNInteger(Whole, Base)
        Numerator = I.BaseTenIntegerToBaseNInteger(Numerator, Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(Denominator, Base)
    else:
        Whole = int(Whole)
        Numerator = int(Numerator)
        Denominator = int(Denominator)
    Common = f'{Whole}:{Numerator}|{Denominator}'
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Simplify Common')
        print()
        Common = input('Enter Common: ')
        Base = input('Enter Base: ')
        Common = I.SimplifyCommon(Common, Base)
        print()
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
