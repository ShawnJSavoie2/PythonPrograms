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
        print()
        EFormat = I.RadixToEFormat(Radix, Base)
        print(EFormat)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
