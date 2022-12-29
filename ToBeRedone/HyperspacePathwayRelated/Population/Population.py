# Python 3.10

# Population

def Population(InitialPopulation, BirthRate, Settlers, Years):
    Population = InitialPopulation
    while Years != 0:
        Population += Population * BirthRate + Settlers
        Years -= 1
    return Population


if __name__ == '__main__':
    import builtins
    # I module
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Population')
        print()
        InitialPopulation = float(input('Enter InitialPopulation: '))
        BirthRate = float(input('Enter BirthRate: '))
        Settlers = float(input('Enter Settlers: '))
        Years = float(input('Enter Years: '))
        print()
        Population = Population(InitialPopulation, BirthRate, Settlers, Years)
        print('Population: ', Population)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
