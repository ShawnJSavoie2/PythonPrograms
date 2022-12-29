
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
        
