# Python 3.9.0

# Common

def Common(Common):


    '''
    Parameters:
    Common: must be a string common ('n', 'n|n' or 'n:n|n').
    '''


    if ':' not in Common and '|' not in Common:
        Common = f'{Common}:0|0'
    if ':' not in Common and '|' in Common:
        Common = f'0:{Common}'
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Common')
        print()
        Common = input('Enter Common: ')
        print()
        Common = I.Common(Common)
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
