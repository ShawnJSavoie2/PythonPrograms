# Python 3.9.0

# PulsarDataAndAveragedTravelTime

class PulsarDataAndAveragedTravelTime:

    def __init__(self):

        self.PulsarOne = {
            'PeriodDerivative' : None,
            'BeforePeriod' : None,
            'BeforeDistance' : None,
            'AfterPeriod' : None,
            'AfterDistance' : None
            }

        self.PulsarTwo = {
            'PeriodDerivative' : None,
            'BeforePeriod' : None,
            'BeforeDistance' : None,
            'AfterPeriod' : None,
            'AfterDistance' : None
            }

        self.PulsarThree = {
            'PeriodDerivative' : None,
            'BeforePeriod' : None,
            'BeforeDistance' : None,
            'AfterPeriod' : None,
            'AfterDistance' : None
            }

        self.PulsarFour = {
            'PeriodDerivative' : None,
            'BeforePeriod' : None,
            'BeforeDistance' : None,
            'AfterPeriod' : None,
            'AfterDistance' : None
            }

        self.PulsarFive = {
            'PeriodDerivative' : None,
            'BeforePeriod' : None,
            'BeforeDistance' : None,
            'AfterPeriod' : None,
            'AfterDistance' : None
            }

        self.PulsarSix = {
            'PeriodDerivative' : None,
            'BeforePeriod' : None,
            'BeforeDistance' : None,
            'AfterPeriod' : None,
            'AfterDistance' : None
            }

        self.PulsarList = [self.PulsarOne, self.PulsarTwo, self.PulsarThree, self.PulsarFour,
                           self.PulsarFive, self.PulsarSix]

        # Note: more pulsars could be added if required. And maybe less could be used if required.

    def AveragedTravelTimeMethod(self):
        SumOfTimes = 0
        for Pulsar in self.PulsarList:
            Pulsar['ReferenceBeforePeriod'] = Pulsar['BeforePeriod'] + (Pulsar['BeforeDistance'] / 299792458.0 * Pulsar['PeriodDerivative'])
            Pulsar['ReferenceAfterPeriod'] = Pulsar['AfterPeriod'] + (Pulsar['AfterDistance'] / 299792458.0 * Pulsar['PeriodDerivative'])
            if Pulsar['ReferenceAfterPeriod'] < Pulsar['ReferenceBeforePeriod']:
                LongerPeriod = Pulsar['ReferenceBeforePeriod']
                ShorterPeriod = Pulsar['ReferenceAfterPeriod']
            else:
                LongerPeriod = Pulsar['ReferenceAfterPeriod']
                ShorterPeriod = Pulsar['ReferenceBeforePeriod']
            Pulsar['Time'] = (LongerPeriod - ShorterPeriod) / Pulsar['PeriodDerivative']
            SumOfTimes += Pulsar['Time']
        self.AveragedTravelTime = SumOfTimes / len(self.PulsarList)


if __name__ == '__main__':
    import builtins
    # I module
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Pulsar Data And Averaged Travel Time')
        print()
    IOPDAATT = I.PulsarDataAndAveragedTravelTime()
    # IOPDAATT means Instance Of PulsarDataAndAveragedTravelTime

    print('PulsarOne:')
    IOPDAATT.PulsarOne['PeriodDerivative'] = float(input('Enter PeriodDerivative: '))
    IOPDAATT.PulsarOne['BeforePeriod'] = float(input('Enter BeforePeriod: '))
    IOPDAATT.PulsarOne['BeforeDistance'] = float(input('Enter BeforeDistance: '))
    IOPDAATT.PulsarOne['AfterPeriod'] = float(input('Enter AfterPeriod: '))
    IOPDAATT.PulsarOne['AfterDistance'] = float(input('Enter AfterDistance: '))

    print()
    print('PulsarTwo:')
    IOPDAATT.PulsarTwo['PeriodDerivative'] = float(input('Enter PeriodDerivative: '))
    IOPDAATT.PulsarTwo['BeforePeriod'] = float(input('Enter BeforePeriod: '))
    IOPDAATT.PulsarTwo['BeforeDistance'] = float(input('Enter BeforeDistance: '))
    IOPDAATT.PulsarTwo['AfterPeriod'] = float(input('Enter AfterPeriod: '))
    IOPDAATT.PulsarTwo['AfterDistance'] = float(input('Enter AfterDistance: '))

    print()
    print('PulsarThree:')
    IOPDAATT.PulsarThree['PeriodDerivative'] = float(input('Enter PeriodDerivative: '))
    IOPDAATT.PulsarThree['BeforePeriod'] = float(input('Enter BeforePeriod: '))
    IOPDAATT.PulsarThree['BeforeDistance'] = float(input('Enter BeforeDistance: '))
    IOPDAATT.PulsarThree['AfterPeriod'] = float(input('Enter AfterPeriod: '))
    IOPDAATT.PulsarThree['AfterDistance'] = float(input('Enter AfterDistance: '))

    print()
    print('PulsarFour:')
    IOPDAATT.PulsarFour['PeriodDerivative'] = float(input('Enter PeriodDerivative: '))
    IOPDAATT.PulsarFour['BeforePeriod'] = float(input('Enter BeforePeriod: '))
    IOPDAATT.PulsarFour['BeforeDistance'] = float(input('Enter BeforeDistance: '))
    IOPDAATT.PulsarFour['AfterPeriod'] = float(input('Enter AfterPeriod: '))
    IOPDAATT.PulsarFour['AfterDistance'] = float(input('Enter AfterDistance: '))

    print()
    print('PulsarFive:')
    IOPDAATT.PulsarFive['PeriodDerivative'] = float(input('Enter PeriodDerivative: '))
    IOPDAATT.PulsarFive['BeforePeriod'] = float(input('Enter BeforePeriod: '))
    IOPDAATT.PulsarFive['BeforeDistance'] = float(input('Enter BeforeDistance: '))
    IOPDAATT.PulsarFive['AfterPeriod'] = float(input('Enter AfterPeriod: '))
    IOPDAATT.PulsarFive['AfterDistance'] = float(input('Enter AfterDistance: '))

    print()
    print('PulsarSix:')
    IOPDAATT.PulsarSix['PeriodDerivative'] = float(input('Enter PeriodDerivative: '))
    IOPDAATT.PulsarSix['BeforePeriod'] = float(input('Enter BeforePeriod: '))
    IOPDAATT.PulsarSix['BeforeDistance'] = float(input('Enter BeforeDistance: '))
    IOPDAATT.PulsarSix['AfterPeriod'] = float(input('Enter AfterPeriod: '))
    IOPDAATT.PulsarSix['AfterDistance'] = float(input('Enter AfterDistance: '))
    print()

    IOPDAATT.AveragedTravelTimeMethod()
    print(f'AveragedTravelTime: {IOPDAATT.AveragedTravelTime}')
    print()
    Answer = input('Would you like to keep using this program? ')
    if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
        break
