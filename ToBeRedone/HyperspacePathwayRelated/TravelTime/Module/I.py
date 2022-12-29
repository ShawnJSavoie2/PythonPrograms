# Python 3.10.0

# TravelTime

def TravelTime(TravelDistance, AccelerationRate, FinalVelocity):

    
    '''
    Parameters:
    TravelDistance: must be an integer or float of a distance measured in light years (LY).
    AcceleationRate: must be an integer or float of an acceleration measured meters per second per second (m/s/s) that can't exceed the velocity of light.
    FinalVelocity: must be an integer or float of a velocity measured in light years per year (LY/Y) that can't exceed the velocity of light.
    '''


    MetersInYear = 9454254955488000
    # The amount of meters traversed in a year at the velocity of light.
    MetersPerSecond = 299792458
    SecondsInYear = 31536000
    # The amount of seconds in a year.
    TravelDistance *= MetersInYear
    FinalVelocity *= MetersPerSecond
    HalfDistance = TravelDistance / 2
    PositiveAccelerationTime = FinalVelocity / AccelerationRate
    PositiveAccelerationDistance = AccelerationRate / 2 * (PositiveAccelerationTime ** 2)
    AccelerationTime = PositiveAccelerationTime * 3
    AccelerationDistance = PositiveAccelerationDistance * 3
    if PositiveAccelerationDistance > HalfDistance:
        TimeToDeceleration = (HalfDistance / (AccelerationRate / 2)) ** (1/2)
        TravelTime = TimeToDeceleration * 2
    else:
        FinalVelocityTime = (TravelDistance - AccelerationDistance) / FinalVelocity
        TimeToDeceleration = PositiveAccelerationTime * 2 + FinalVelocityTime
        TravelTime = AccelerationTime + FinalVelocityTime
    TravelTime /= SecondsInYear
    PositiveAccelerationTime /= SecondsInYear
    PositiveAccelerationDistance /= MetersInYear
    AccelerationTime /= SecondsInYear
    AccelerationDistance /= MetersInYear
    try:
        FinalVelocityTime /= SecondsInYear
    except:
        FinalVelocityTime = 0
    TimeToDeceleration /= SecondsInYear
    Dictionary = {
        'TravelTime': f'{TravelTime:} years, {TravelTime * 12} months or {TravelTime * 365} days.',
        'PositiveAccelerationTime': f'{PositiveAccelerationTime:} years, {PositiveAccelerationTime * 12} months or {PositiveAccelerationTime * 365} days.',
        'PositiveAccelerationDistance': f'{PositiveAccelerationDistance:} light years, {PositiveAccelerationDistance * 12} light months or {PositiveAccelerationDistance * 365} light days.',
        'AccelerationTime': f'{AccelerationTime:} years, {AccelerationTime * 12} months or {AccelerationTime * 365} days.', 
        'AccelerationDistance': f'{AccelerationDistance:} light years, {AccelerationDistance * 12} light months or {AccelerationDistance * 365} light days.',
        'FinalVelocityTime': f'{FinalVelocityTime:} years, {FinalVelocityTime * 12} months or {FinalVelocityTime * 365} days.', 
        'TimeToDeceleration': f'{TimeToDeceleration:} years, {TimeToDeceleration * 12} months or {TimeToDeceleration * 365} days.'
        }
    return Dictionary


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Travel Time')
        print()
        TravelDistance = float(input('Enter Distance: '))
        AccelerationRate = float(input('Enter Acceleration Rate: '))
        FinalVelocity = float(input('Enter Final Velocity: '))
        print()
        TravelTime = I.TravelTime(TravelDistance, AccelerationRate, FinalVelocity)
        for key, value in TravelTime.items():
            print(key, value)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
        
