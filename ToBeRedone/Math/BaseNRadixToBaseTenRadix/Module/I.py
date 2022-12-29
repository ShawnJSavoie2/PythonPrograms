
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
        
