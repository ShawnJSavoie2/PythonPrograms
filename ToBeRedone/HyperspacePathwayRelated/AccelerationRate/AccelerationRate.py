# Python 3.10.0

# Acceleration Rate

def AccelerationRate(FinalVelocity, TravelDistance, TravelTime):


    '''
    Parameters:
    FinalVelocity: must be an integer or float of a velocity measured in light years per year (LY/Y) that can't exceed 1 LY/Y.
    TravelDistance: must be an integer or float of a distance measured in light years (LY).
    TravelTime: must be an integer or float of a time measured in years (Y).
    '''


    if TravelTime == TravelDistance:
        Dictionary = {'AccelerationRate': 'INSTANTANEOUS ACCELERATION- FOR THE WIN!'}
        return Dictionary
    if TravelTime < TravelDistance:
        Dictionary = {'AccelerationRate': 'IMPOSSIBLE ACCELERATION- FOR THE LOSE!'}
        return Dictionary
    MetersPerSecond = 299792458
    MetersInYear = 9454254955488000
    # The amount of meters traversed in a year at the velocity of light.
    SecondsInYear = 31536000
    # The amount of seconds in a year.
    FinalVelocity *= MetersPerSecond
    TravelDistance *= MetersInYear
    TravelTime = round(TravelTime * SecondsInYear)
    AccelerationRateIncrease = 1
    WorkingAccelerationRate = 1
    while True:
        PositiveAccelerationTime = FinalVelocity / WorkingAccelerationRate
        PositiveAccelerationDistance = WorkingAccelerationRate / 2 * (PositiveAccelerationTime ** 2)
        AccelerationTime = PositiveAccelerationTime * 3
        AccelerationDistance = PositiveAccelerationDistance * 3
        VelocityTime = (TravelDistance - AccelerationDistance) / FinalVelocity
        WorkingTime = AccelerationTime + VelocityTime
        WorkingTime = round(WorkingTime)
        if WorkingTime > TravelTime:
            WorkingAccelerationRate += AccelerationRateIncrease
        elif WorkingTime == TravelTime:
            break
        else: # WorkingAcceleration < TravelTime:
            WorkingAccelerationRate -= AccelerationRateIncrease
            AccelerationRateIncrease /= 10
            WorkingAccelerationRate += AccelerationRateIncrease
    AccelerationRate = WorkingAccelerationRate
    PositiveAccelerationTime /= SecondsInYear
    PositiveAccelerationDistance /= MetersInYear
    AccelerationTime /= SecondsInYear
    AccelerationDistance /= MetersInYear
    VelocityTime /= SecondsInYear
    Dictionary = {
        'AccelerationRate': f'{AccelerationRate} m/s/s.',
        'PositiveAccelerationTime': f'{PositiveAccelerationTime} years, {PositiveAccelerationTime * 12} months or {PositiveAccelerationTime * 365} days.',
        'PositiveAccelerationDistance': f'{PositiveAccelerationDistance} light years, {PositiveAccelerationDistance * 12} light months or {PositiveAccelerationDistance * 365} light days.',
        'AccelerationTime': f'{AccelerationTime} years, {AccelerationTime * 12} months or {AccelerationTime * 365} days.',
        'AccelerationDistance': f'{AccelerationDistance} light years, {AccelerationDistance * 12} light months or {AccelerationDistance * 365} light days.',
        'VelocityTime': f'{VelocityTime} years, {VelocityTime * 12} months or {VelocityTime * 365} days.'
        }
    return Dictionary


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('AccelerationRate')
        print()
        FinalVelocity = float(input('Enter FinalVelocity: '))
        TravelDistance = float(input('Enter Distance: '))
        TravelTime = float(input('Enter Time: '))
        print()
        AccelerationRate = I.AccelerationRate(FinalVelocity, TravelDistance, TravelTime)
        for key, value in AccelerationRate.items():
            print(key, value)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
