# Python 3.9.0

# ParseExpression


def ParseExpression(Expression, Fraction, Base):


    '''
    Parameters:
    Expression: must be a string expression containing only elements from DigitsPointBar,
    SeperatorsAndSpace and OperatorsAndParentheses.
    Fraction: must be a string term: Radix or Common.
    Base: must be a string integer that's one number that's between and including 2 and 16.

    Dependencies:
    Programmer's:
    Radix
    Common
    CommonToRadix
    BaseNRadixToBaseTenRadix
    '''


    DigitsPointBar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
                      '.', ':', '|']
    SeparatorsAndSpace = [',', '_', ' ']
    OperatorsAndParentheses = ['+', '-', '×', '÷', '˄', '˅', 'T', '(', ')']
    Number = ''
    ExpressionList = []
    for Element in enumerate(Expression):
        if Element[1] in SeparatorsAndSpace:
            continue
        if Element[1] in OperatorsAndParentheses:
            if Expression[(Element[0] - 1)] == 'e':
                Number = f'{Number}{Element[1]}'
            elif Expression[(Element[0] + 1)] in DigitsPointBar:
                if Number != '':
                    ExpressionList.append(Number)
                    Number = Element[1]
                else:
                    Number = Element[1]
            else:
                if Number != '':
                    ExpressionList.append(Number)
                    ExpressionList.append(Element[1])
                    Number = ''
                else:
                    ExpressionList.append(Element[1])
        else:
            Number = f'{Number}{Element[1]}'
    # In case for loop ends before adding.
    if Number != '':
        ExpressionList.append(Number)
    if Fraction == 'Rad':
        WorkingExpressionList = []
        WorkingNumber = ''
        for Element in ExpressionList:
            if Element in OperatorsAndParentheses:
                WorkingExpressionList.append(Element)
            else:
                if 'e' in Element:
                    WorkingNumber = I.EFormatToRadix(Element, Base)
                    WorkingExpressionList.append(WorkingNumber)
                else:
                    WorkingNumber = I.Radix(Element)
                    WorkingExpressionList.append(WorkingNumber)
        ExpressionList = WorkingExpressionList
    else: # Fraction == 'Com'
        WorkingExpressionList = []
        WorkingNumber = ''
        for Element in ExpressionList:
            if Element in OperatorsAndParentheses:
                WorkingExpressionList.append(Element)
            else:
                WorkingNumber = I.Common(Element)
                WorkingNumber = I.CommonToRadix(WorkingNumber, Base)
                WorkingExpressionList.append(WorkingNumber)
        ExpressionList = WorkingExpressionList
    if Base != '10':
        WorkingExpressionList = []
        WorkingNumber = ''
        for Element in ExpressionList:
            if Element in OperatorsAndParentheses:
                WorkingExpressionList.append(Element)
            else:
                WorkingNumber = I.BaseNRadixToBaseTenRadix(Element, Base)
                WorkingExpressionList.append(WorkingNumber)
        ExpressionList = WorkingExpressionList
    return ExpressionList


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Parse Expression')
        print()
        Expression = input('Enter Expression: ')
        Fraction = input('Enter Fraction: ')
        Base = input('Enter Base: ')
        ExpressionList = I.ParseExpression(Expression, Fraction, Base)
        print()
        print(ExpressionList)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

        
