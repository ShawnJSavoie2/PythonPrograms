# Python 3.10

# YearsOfGrowth

def YearsOfGrowth(InitialPopulation, BirthRate, Settlers, ReferencePopulation):
    InterimPopulation = InitialPopulation
    YearsOfGrowth = 0
    while InterimPopulation < ReferencePopulation:
        InterimPopulation += InterimPopulation * BirthRate + Settlers
        YearsOfGrowth += 1
    return YearsOfGrowth, InterimPopulation


if __name__ == '__main__':
    import builtins
    # I module
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Years Of Growth')
        print()
        InitialPopulation = float(input('Enter InitialPopulation: '))
        BirthRate = float(input('Enter BirthRate: '))
        Settlers = float(input('Enter Settlers: '))
        ReferencePopulation = float(input('ReferencePopulation: '))
        print()
        YearsOfGrowth, InterimPopulation = YearsOfGrowth(InitialPopulation, BirthRate, Settlers, ReferencePopulation)
        print('YearsOfGrowth: ', YearsOfGrowth)
        print('InterimPopulation: ', InterimPopulation)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
