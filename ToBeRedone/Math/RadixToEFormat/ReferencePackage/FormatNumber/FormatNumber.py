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


