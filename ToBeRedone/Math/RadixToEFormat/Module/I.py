
# Python 3.9.0

# RadixToEFormat

def RadixToEFormat(Radix, Base):


    '''
    Parameters:
    Radix: must be a string Radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseTenIntegerToBaseNInteger
    FormatNumber
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    if Whole == '0':
        Zeros = 0
        for Digit in Fraction:
            if Digit == '0':
                Zeros += 1
            else:
                break
        if Zeros >= 4:
            Exponent = Zeros + 1
            if (len(Fraction) - Zeros) > 1:
                Fraction = f'{Fraction[Zeros]}.{Fraction[(Zeros + 1):]}'
            else:
                Fraction = Fraction[Zeros]
            if Base != '10':
                Exponent = I.BaseTenIntegerToBaseNInteger(Exponent, Base)
            Fraction = I.FormatNumber(Fraction)
            EFormat = f'{Fraction}e-{Exponent}'
            return EFormat
    else: # Whole != '0'
        if Fraction == '0':
            Zeros = 0
            for Digit in reversed(Whole):
                if Digit == '0':
                    Zeros += 1
                else:
                    break
            if Zeros >= 4:
                Exponent = len(Whole) - 1
                if (len(Whole) - Zeros) > 1:
                    Whole = f'{Whole[0]}.{Whole[1:-Zeros]}'
                else:
                    Whole = Whole[0]
                if Base != '10':
                    Exponent = I.BaseTenIntegerToBaseNInteger(Exponent, Base)
                Whole = I.FormatNumber(Whole)
                EFormat = f'{Whole}e+{Exponent}'
                return EFormat
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('RadixToEFormat')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        EFormat = I.RadixToEFormat(Radix, Base)
        print()
        print(EFormat)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        


# Python 3.9.0

# RadixToEFormat

def RadixToEFormat(Radix, Base):


    '''
    Parameters:
    Radix: must be a string Radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseTenIntegerToBaseNInteger
    FormatNumber
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    if Whole == '0':
        Zeros = 0
        for Digit in Fraction:
            if Digit == '0':
                Zeros += 1
            else:
                break
        if Zeros >= 4:
            Exponent = Zeros + 1
            if (len(Fraction) - Zeros) > 1:
                Fraction = f'{Fraction[Zeros]}.{Fraction[(Zeros + 1):]}'
            else:
                Fraction = Fraction[Zeros]
            if Base != '10':
                Exponent = I.BaseTenIntegerToBaseNInteger(Exponent, Base)
            Fraction = I.FormatNumber(Fraction)
            EFormat = f'{Fraction}e-{Exponent}'
            return EFormat
    else: # Whole != '0'
        if Fraction == '0':
            Zeros = 0
            for Digit in reversed(Whole):
                if Digit == '0':
                    Zeros += 1
                else:
                    break
            if Zeros >= 4:
                Exponent = len(Whole) - 1
                if (len(Whole) - Zeros) > 1:
                    Whole = f'{Whole[0]}.{Whole[1:-Zeros]}'
                else:
                    Whole = Whole[0]
                if Base != '10':
                    Exponent = I.BaseTenIntegerToBaseNInteger(Exponent, Base)
                Whole = I.FormatNumber(Whole)
                EFormat = f'{Whole}e+{Exponent}'
                return EFormat
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('RadixToEFormat')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        EFormat = I.RadixToEFormat(Radix, Base)
        print()
        print(EFormat)
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


