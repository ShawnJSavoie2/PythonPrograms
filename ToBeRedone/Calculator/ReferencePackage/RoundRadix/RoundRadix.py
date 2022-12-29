# Python 3.9.0

# RoundRadix

def RoundRadix(Radix, Base, Place):


    '''
    Parameters:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    Place: must be a string integer that's in a base equal to the Base.

    Dependencies:
    Programmer's:
    BaseNIntegerToBaseTenInteger
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    if Base == '10':
        if len(Fraction) > int(Place):
            Fraction = f'0.{Fraction}'
            Fraction = round(float(Fraction), int(Place))
            Radix = str(float(Whole) + Fraction)
    else:
        Place = I.BaseNIntegerToBaseTenInteger(Place, Base)
        if len(Fraction) > int(Place):
            LengthOfWhole = len(Whole)
            LengthOfFraction = len(Fraction)
            LengthOfNumber = LengthOfWhole + LengthOfFraction
            Number = f'0{Whole}{Fraction}'
            Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
                      'F']
            HalfBase = round(int(Base) / 2)
            UsedDigits = Digits[:int(Base)]
            HalfOfDigits = UsedDigits[:HalfBase]
            Count = LengthOfFraction - int(Place)
            NumberList = []
            for Digit in reversed(Number):
                NumberList.append(Digit)
            CurrentDigit = NumberList[0]
            for Element in enumerate(NumberList):
                if Count == 0:
                    if CurrentDigit != Digits[int(Base)]:
                        break
                    else:
                        NumberList[Element[0]] = '0'
                        IndexOfFollowingDigit = Digits.index(NumberList[(Element[0] + 1)])
                        NumberList[(Element[0] + 1)] = Digits[(IndexOfFollowingDigit + 1)]
                        CurrentDigit = NumberList[(Element[0] + 1)]
                else:
                    if CurrentDigit in HalfOfDigits:
                        NumberList[Element[0]] = '0'
                        CurrentDigit = NumberList[(Element[0] + 1)]
                        Count -= 1
                    else:
                        NumberList[Element[0]] = '0'
                        IndexOfFollowingDigit = Digits.index(NumberList[(Element[0] + 1)])
                        NumberList[(Element[0] + 1)] = Digits[(IndexOfFollowingDigit + 1)]
                        CurrentDigit = NumberList[(Element[0] + 1)]
                        Count -= 1
            NumberList.reverse()
            if NumberList[0] == '0':
                NumberList = NumberList[1:]
            Difference = len(NumberList) - LengthOfNumber
            if Difference == 0:
                NumberList.insert(LengthOfWhole, '.')
            else:
                LengthOfWhole += Difference
                NumberList.insert(LengthOfWhole, '.')
            while NumberList[-1] == '0':
                NumberList = NumberList[:-1]
            Number = ''
            for Element in NumberList:
                Number = f'{Number}{Element}'
            if Number[-1] == '.':
                Radix = str(float(Number))
            else:
                Radix = Number
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Round Radix')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        Place = input('Enter Place: ')
        print()
        Radix = I.RoundRadix(Radix, Base, Place)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
