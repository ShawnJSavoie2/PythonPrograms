# Python 3.9.0

# Calculate

def Calculate(ExpressionList):


    '''
    Parameters:
    ExpressionList: must be a list containing at least two string floats and one string operator.
    '''


    Operators = ['+', '-', '×', '÷', '˄', '˅', 'T']
    OperatorsAndParentheses = ['+', '-', '×', '÷', '˄', '˅', 'T', '(', ')']
    OperandOne = ''
    Operator = ''
    OperandTwo = ''
    ForIndex = 0
    for Element in ExpressionList:
        if Element not in OperatorsAndParentheses:
            if OperandOne == '':
                OperandOne = Element
            else:
                OperandTwo = Element
        if Element in Operators:
            Operator = Element
        if Element == '(':
            Result = I.Calculate(ExpressionList[(ForIndex + 1):])
            if OperandOne == '':
                OperandOne = Result
            else:
                OperandTwo = Result
            GoodToGo = 'no'
            LeftParentheses = 0
            RightParentheses = 0
            WhileIndex = ForIndex
            while GoodToGo == 'no':
                if ExpressionList[WhileIndex] == '(':
                    LeftParentheses = LeftParentheses + 1
                if ExpressionList[WhileIndex] == ')':
                    RightParentheses = RightParentheses + 1
                ExpressionList[WhileIndex] = ''
                if LeftParentheses != RightParentheses:
                    GoodToGo = 'no'
                    WhileIndex = WhileIndex + 1
                else:
                    GoodToGo = 'yes'
        if Element == ')':
            return OperandOne
        if OperandOne != '' and Operator != '' and OperandTwo != '':
            if Operator == '+':
                OperandOne = float(OperandOne) + float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '-':
                OperandOne = float(OperandOne) - float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '×':
                OperandOne = float(OperandOne) * float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '÷':
                OperandOne = float(OperandOne) / float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '˄':
                OperandOne = float(OperandOne) ** float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '˅':
                OperandOne = float(OperandOne) ** (1 / float(OperandTwo))
                Operator = ''
                OperandTwo = ''
            elif Operator == 'T':
                OperandOne = float(I.GetExponent(float(OperandOne), float(OperandTwo)))
                Operator = ''
                OperandTwo = ''
        ForIndex = ForIndex + 1
    return str(OperandOne)


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Calculate')
        print()
        ExpressionList = input('Enter ExpressionList: ')
        print()
        # A list with at least two string floats and one string operator that are separated by commas
        ExpressionList = ExpressionList.split(', ')
        OperandOne = I.Calculate(ExpressionList)
        print(OperandOne)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
