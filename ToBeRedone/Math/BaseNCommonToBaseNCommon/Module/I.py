
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
        Radix = I.BaseTenRadixToBaseNRadix(Radix, Base)
        print()
        print(Radix)
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

# GetExponent

def GetExponent(Root, Power):


    '''
    Parameters:
    Power: must be a literal integer or float.
    Root: must be a literal integer or float.
    '''


    Exponent = 1
    while Power != Root:
        Power = Power / Root
        Exponent += 1
    return Exponent


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Get Exponent')
        print()
        Root = float(input('Enter Root: '))
        Power = float(input('Enter Power: '))
        Exponent = I.GetExponent(Root, Power)
        print()
        print(Exponent)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# SimplifyRoundedCommon

def SimplifyRoundedCommon(Common, Base, Divisor):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') with a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    Divisor: must be a string integer.

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
    Divisor = int(Divisor)
    GoodToGo = 'No'
    while GoodToGo == 'No':
        if Divisor <= Numerator:
            if Numerator % Divisor == 0 and Denominator % Divisor == 0:
                Numerator /= Divisor
                Denominator /= Divisor
            else:
                GoodToGo = 'Yes'
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
        print('Simplify Rounded Common')
        print()
        Common = input('Enter Common: ')
        Base = input('Enter Base: ')
        Divisor = input('Enter Divisor: ')
        Common = I.SimplifyRoundedCommon(Common, Base, Divisor)
        print()
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
        

# Python 3.9.0

# Common

def Common(Common):


    '''
    Parameters:
    Common: must be a string common ('n', 'n|n' or 'n:n|n').
    '''


    if ':' not in Common and '|' not in Common:
        Common = f'{Common}:0|0'
    if ':' not in Common and '|' in Common:
        Common = f'0:{Common}'
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Common')
        print()
        Common = input('Enter Common: ')
        Common = I.Common(Common)
        print()
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# CommonToRadix

def CommonToRadix(Common, Base):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseNIntegerToBaseTenInteger,
    BaseTenRadixToBaseNRadix
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
    if Numerator == '0' and Denominator == '0':
        Fraction = 0.0
    else:
        Fraction = int(Numerator) / int(Denominator)
    Radix = str(int(Whole) + Fraction)
    if Base != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, Base)
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Common To Radix')
        print()
        Common = input('Enter Common: ')
        Base = input('Enter Base: ')
        Radix = I.CommonToRadix(Common, Base)
        print()
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        

# Python 3.9.0

# FormatNumber

def FormatNumber(Number):


    '''
    Parameters:
    Number: must be a string number.
    '''


    if '.' in Number:
        if Number[0] == '.':
            Number = f'0{Number}'
        IndexOfPoint = Number.index('.')
        Whole = Number[:IndexOfPoint]
        Fraction = Number[(IndexOfPoint + 1):]
        # Whole part.
        if Whole != '0':
            Reversed = ''
            for Digit in reversed(Whole):
                Reversed = f'{Reversed}{Digit}'
            WorkingReversed = ''
            Count = 0
            for Digit in Reversed:
                if Count == 3:
                    WorkingReversed = f'{WorkingReversed},{Digit}'
                    Count = 1
                else:
                    WorkingReversed = f'{WorkingReversed}{Digit}'
                    Count += 1
            Whole = ''
            for Digit in reversed(WorkingReversed):
                Whole = f'{Whole}{Digit}'
        # Fraction part.
        if Fraction != '' or Fraction != '0':
            Zeros = ''
            for Digit in Fraction:
                if Digit == '0':
                    Zeros = f'{Zeros}{Digit}'
                else:
                    break
            Fraction = Fraction[len(Zeros):]
            Reversed = ''
            for Digit in reversed(Fraction):
                Reversed = f'{Reversed}{Digit}'
            WorkingReversed = ''
            Count = 0
            for Digit in Reversed:
                if Count == 3:
                    WorkingReversed = f'{WorkingReversed}_{Digit}'
                    Count = 1
                else:
                    WorkingReversed = f'{WorkingReversed}{Digit}'
                    Count += 1
            Fraction = ''
            for Element in reversed(WorkingReversed):
                Fraction = f'{Fraction}{Element}'
            Fraction = f'{Zeros}{Fraction}'
        # Whole and fraction parts.
        Number = f'{Whole}.{Fraction}'
    elif ':' in Number:
        if Number[0] == ':':
            Number = f'0{Number}'
        IndexOfColon = Number.index(':')
        Whole = Number[:IndexOfColon]
        Fraction = Number[(IndexOfColon + 1):]
        # Whole part
        if Whole != '0':
            Reversed = ''
            for Element in reversed(Whole):
                Reversed = f'{Reversed}{Element}'
            WorkingReversed = ''
            Count = 0
            for Element in Reversed:
                if Count == 3:
                    WorkingReversed = f'{WorkingReversed},{Element}'
                    Count = 1
                else:
                    WorkingReversed = f'{WorkingReversed}{Element}'
                    Count += 1
            Whole = ''
            for Element in reversed(WorkingReversed):
                Whole = f'{Whole}{Element}'
        # Fraction part
        if Fraction != '' or Fraction != '0':
            Reversed = ''
            for Element in reversed(Fraction):
                Reversed = f'{Reversed}{Element}'
            WorkingReversed = ''
            Count = 0
            for Element in Reversed:
                if Element == '|':
                    WorkingReversed = f'{WorkingReversed}{Element}'
                    Count = 0
                elif Count == 3:
                    WorkingReversed = f'{WorkingReversed}_{Element}'
                    Count = 1
                else:
                    WorkingReversed = f'{WorkingReversed}{Element}'
                    Count += 1
            Fraction = ''
            for Element in reversed(WorkingReversed):
                Fraction = f'{Fraction}{Element}'
        Number = f'{Whole}:{Fraction}'
    elif '|' in Number:
        Reversed = ''
        for Element in reversed(Number):
            Reversed = f'{Reversed}{Element}'
        WorkingReversed = ''
        Count = 0
        for Element in Reversed:
            if Element == '|':
                WorkingReversed = f'{WorkingReversed}{Element}'
                Count = 0
            elif Count == 3:
                WorkingReversed = f'{WorkingReversed}_{Element}'
                Count = 1
            else:
                WorkingReversed = f'{WorkingReversed}{Element}'
                Count += 1
        Number = ''
        for Element in reversed(WorkingReversed):
            Number = f'{Number}{Element}'
    else:
        Reversed = ''
        for Element in reversed(Number):
            Reversed = f'{Reversed}{Element}'
        WorkingReversed = ''
        Count = 0
        for Element in Reversed:
            if Count == 3:
                WorkingReversed = f'{WorkingReversed},{Element}'
                Count = 1
            else:
                WorkingReversed = f'{WorkingReversed}{Element}'
                Count += 1
        Number = ''
        for Element in reversed(WorkingReversed):
            Number = f'{Number}{Element}'
    return Number


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Format Number')
        print()
        Number = input('Enter Number: ')
        Number = I.FormatNumber(Number)
        print()
        print(Number)
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
