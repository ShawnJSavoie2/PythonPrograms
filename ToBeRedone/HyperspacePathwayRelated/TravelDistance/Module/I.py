# Python 3.10.0

# TravelDistance

def TravelDistance(FinalVelocity, AccelerationRate, TravelTime):


    '''
    Parameters:
    FinalVelocity: must be an integer or float of a velocity measured in light years (LY).
    AccelerationRate: must be an integer or float of an acceleration measured in m/s/s.
    TravelTime: must be an integer or float of a time measured in years (Y).
    '''

    MetersPerSecond = 299792458
    SecondsInYear = 31536000
    # The amount of seconds in a year.
    MetersInYear = 9454254955488000
    # The amount of meters traversed in a year at the velocity of light.
    FinalVelocity *= MetersPerSecond
    TravelTime *= SecondsInYear
    PositiveAccelerationTime = FinalVelocity / AccelerationRate
    PositiveAccelerationDistance = AccelerationRate / 2 * (PositiveAccelerationTime ** 2)
    AccelerationTime = PositiveAccelerationTime * 3
    AccelerationDistance = PositiveAccelerationDistance * 3
    FinalVelocityTime = TravelTime - AccelerationTime
    FinalVelocityDistance = FinalVelocityTime * FinalVelocity
    TravelDistance = AccelerationDistance + FinalVelocityDistance
    TravelDistance /= MetersInYear
    PositiveAccelerationTime /= SecondsInYear
    PositiveAccelerationDistance /= MetersInYear
    AccelerationTime /= SecondsInYear
    AccelerationDistance /= MetersInYear
    FinalVelocityTime /= SecondsInYear
    FinalVelocityDistance /= MetersInYear
    Dictionary = {
        'TravelDistance': f'{TravelDistance} light years, {TravelDistance * 12} light months or {TravelDistance * 365} light days.',
        'PositiveAccelerationTime': f'{PositiveAccelerationTime} years, {PositiveAccelerationTime * 12} months or {PositiveAccelerationTime * 365} days.',
        'PositiveAccelerationDistance': f'{PositiveAccelerationDistance} light years, {PositiveAccelerationDistance * 12} light months or {PositiveAccelerationDistance * 365} light days.',
        'AccelerationTime': f'{AccelerationTime} years, {AccelerationTime * 12} months or {AccelerationTime * 365} days.',
        'AccelerationDistance': f'{AccelerationDistance} light years, {AccelerationDistance * 12} light months or {AccelerationDistance * 365} light days.',
        'FinalVelocityTime': f'{FinalVelocityTime} years, {FinalVelocityTime * 12} months or {FinalVelocityTime * 365} days.',
        'FinalVelocityDistance': f'{FinalVelocityDistance} light years, {FinalVelocityDistance * 12} light months or {FinalVelocityDistance * 365} light days.'
        }
    return Dictionary


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Travel Distance')
        print()
        FinalVelocity = float(input('Enter FinalVelocity: '))
        AccelerationRate = float(input('Enter AccelerationRate: '))
        TravelTime = float(input('Enter TravelTime: '))
        print()
        TravelDistance = I.TravelDistance(FinalVelocity, AccelerationRate, TravelTime)
        for key, value in TravelDistance.items():
            print(key, value)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
