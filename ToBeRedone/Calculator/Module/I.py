
# Tkinter | Python 3.9.0

# Calculator

class Calculator:
    def __init__(self):
        # WINDOW
        self.Window = U.Tk.Tk()
        self.Window.title('Calculator')
        W = 600
        H = 450
        SW = self.Window.winfo_screenwidth()
        SH = self.Window.winfo_screenheight()
        X = int((SW - W) / 2)
        Y = int((SH - H) / 2)
        self.Window.geometry(f'{W}x{H}+{X}+{Y}')
        self.Window.minsize(width = W, height = H)
        self.Window.bind('<Configure>', self.ResizeFont)

        # VARIABLES
        self.Mode = 'Calculator'
        self.Base = '10'
        self.Fraction = 'Rad'
        self.RoundCommon = '_  _'
        self.Radix = ''
        self.BaseOfRadix = ''
        self.Common = ''
        self.BaseOfCommon = ''
        self.Input = ''
        self.Output = ''
        self.InputStorage = {
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
            '9': '',
            '10': '',
            '11': '',
            '12': '',
            '13': '',
            '14': '',
            '15': '',
            '16': ''
            }
        self.OutputStorage = {
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
            '9': '',
            '10': '',
            '11': '',
            '12': '',
            '13': '',
            '14': '',
            '15': '',
            '16': ''
            }
        self.RoundRadixStorage = {
            '2': '_',
            '3': '_',
            '4': '_',
            '5': '_',
            '6': '_',
            '7': '_',
            '8': '_',
            '9': '_',
            '10': '_',
            '11': '_',
            '12': '_',
            '13': '_',
            '14': '_',
            '15': '_',
            '16': '_'
            }
        self.RootDenominatorStorage = {
            '2': '_',
            '3': '_',
            '4': '_',
            '5': '_',
            '6': '_',
            '7': '_',
            '8': '_',
            '9': '_',
            '10': '_',
            '11': '_',
            '12': '_',
            '13': '_',
            '14': '_',
            '15': '_',
            '16': '_'
            }
        self.PowerDenominatorStorage = {
            '2': '_',
            '3': '_',
            '4': '_',
            '5': '_',
            '6': '_',
            '7': '_',
            '8': '_',
            '9': '_',
            '10': '_',
            '11': '_',
            '12': '_',
            '13': '_',
            '14': '_',
            '15': '_',
            '16': '_'
            }
        self.AcceptableBases = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                '14', '15', '16']
        self.Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
                       'F']
        self.BaseDiagonal = 750
        self.BaseFontSize = 9
        self.FontSize = U.font.Font(size = str(self.BaseFontSize))
        self.Style = U.ttk.Style()
        self.Style.configure('TButton', font = self.FontSize)


        # WIDGITS
        self.Frame = U.ttk.Frame(self.Window)
        self.Frame.grid(
            column = 0,
            row = 0,
            sticky = 'wens'
            )
        self.Window.columnconfigure(0, weight = 4)
        self.Window.rowconfigure(0, weight = 3)


        #ROW ZERO
        self.InputScreen = U.ttk.Label(
            self.Frame,
            text = self.Input,
            anchor = 'w',
            font = self.FontSize,
            )
        self.InputScreen.grid(
            column = 0,
            row = 0,
            columnspan = 10,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(0, weight = 3)


        # ROW ONE
        self.OutputScreen = U.ttk.Label(
            self.Frame,
            text = self.Output,
            anchor = 'e',
            borderwidth = 1
            )
        self.OutputScreen.grid(
            column = 0,
            row = 1,
            columnspan = 10,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(1, weight = 3)


        # ROW TWO
        self.BaseDisplayButton = U.ttk.Button(
            self.Frame,
            text = self.Base,
            state = 'disabled'
            )
        self.BaseDisplayButton.grid(
            column = 0,
            row = 2,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(2, weight = 3)


        self.FractionDisplayButton = U.ttk.Button(
            self.Frame,
            text = self.Fraction,
            state = 'disabled'
            )
        self.FractionDisplayButton.grid(
            column = 1,
            row = 2,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(1, weight = 4)
        self.Frame.rowconfigure(2, weight = 3)


        self.RoundRadixDisplayButton = U.ttk.Button(
            self.Frame,
            text = self.RoundRadixStorage[self.Base],
            state = 'disabled'
            )
        self.RoundRadixDisplayButton.grid(
            column = 2,
            row = 2,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(2, weight = 4)
        self.Frame.rowconfigure(2, weight = 3)


        self.RoundCommonDisplayButton = U.ttk.Button(
            self.Frame,
            text = self.RoundCommon,
            state = 'disabled'
            )
        self.RoundCommonDisplayButton.grid(
            column = 3,
            row = 2,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(3, weight = 4)
        self.Frame.rowconfigure(2, weight = 3)


        self.OffButton = U.ttk.Button(
            self.Frame,
            text = 'Off',
            command = lambda: self.OffMethod()
            )
        self.OffButton.grid(
            column = 9,
            row = 2,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(9, weight = 4)
        self.Frame.rowconfigure(2, weight = 3)


        # ROW THREE
        self.BaseButton = U.ttk.Button(
            self.Frame,
            text = 'Base',
            command = lambda: self.BaseMethod()
            )
        self.BaseButton.grid(
            column = 0,
            row = 3,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(3, weight = 3)


        self.FractionButton = U.ttk.Button(
            self.Frame,
            text = 'Fraction',
            command = lambda: self.FractionMethod()
            )
        self.FractionButton.grid(
            column = 1,
            row = 3,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(1, weight = 4)
        self.Frame.rowconfigure(3, weight = 3)


        self.RoundRadixButton = U.ttk.Button(
            self.Frame,
            text = '(R)',
            command = lambda: self.RoundRadixMethod()
            )
        self.RoundRadixButton.grid(
            column = 2,
            row = 3,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(2, weight = 4)
        self.Frame.rowconfigure(3, weight = 3)


        self.RoundCommonButton = U.ttk.Button(
            self.Frame,
            text = '(C)',
            command = lambda: self.RoundCommonMethod()
            )
        self.RoundCommonButton.grid(
            column = 3,
            row = 3,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(3, weight = 4)
        self.Frame.rowconfigure(3, weight = 3)


        # ROW FOUR
        self.RadToRadButton = U.ttk.Button(
            self.Frame,
            text = 'R -> R',
            command = lambda: self.RadToRadMethod()
            )
        self.RadToRadButton.grid(
            column = 0,
            row = 4,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(4, weight = 3)


        self.ComToRadButton = U.ttk.Button(
            self.Frame,
            text = 'C -> R',
            command = lambda: self.ComToRadMethod()
            )
        self.ComToRadButton.grid(
            column = 1,
            row = 4,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(1, weight = 4)
        self.Frame.rowconfigure(4, weight = 3)


        self.RadToComButton = U.ttk.Button(
            self.Frame,
            text = 'R -> C',
            state = 'disabled',
            command = lambda: self.RadToComMethod()
            )
        self.RadToComButton.grid(
            column = 2,
            row = 4,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(2, weight = 4)
        self.Frame.rowconfigure(4, weight = 3)


        self.ComToComButton = U.ttk.Button(
            self.Frame,
            text = 'C -> C',
            state = 'disabled',
            command = lambda: self.ComToComMethod()
            )
        self.ComToComButton.grid(
            column = 3,
            row = 4,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(3, weight = 4)
        self.Frame.rowconfigure(4, weight = 3)


        # ROW FIVE
        self.SinButton = U.ttk.Button(
            self.Frame,
            text = 'Sin',
            command = lambda: self.SinMethod()
            )
        self.SinButton.grid(
            column = 0,
            row = 5,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(5, weight = 3)


        self.CosButton = U.ttk.Button(
            self.Frame,
            text = 'Cos',
            command = lambda: self.CosMethod()
            )
        self.CosButton.grid(
            column = 1,
            row = 5,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(1, weight = 4)
        self.Frame.rowconfigure(5, weight = 3)


        self.TanButton = U.ttk.Button(
            self.Frame,
            text = 'Tan',
            command = lambda: self.TanMethod()
            )
        self.TanButton.grid(
            column = 2,
            row = 5,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(2, weight = 4)
        self.Frame.rowconfigure(5, weight = 3)


        self.SinAButton = U.ttk.Button(
            self.Frame,
            text = 'SinA',
            command = lambda: self.SinAMethod()
            )
        self.SinAButton.grid(
            column = 3,
            row = 5,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(3, weight = 4)
        self.Frame.rowconfigure(5, weight = 3)


        self.CosAButton = U.ttk.Button(
            self.Frame,
            text = 'CosA',
            command = lambda: self.CosAMethod()
            )
        self.CosAButton.grid(
            column = 4,
            row = 5,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(4, weight = 4)
        self.Frame.rowconfigure(5, weight = 3)


        self.TanAButton = U.ttk.Button(
            self.Frame,
            text = 'TanA',
            command = lambda: self.TanAMethod()
            )
        self.TanAButton.grid(
            column = 5,
            row = 5,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(5, weight = 4)
        self.Frame.rowconfigure(5, weight = 3)


        # ROW SIX
        self.PiButton = U.ttk.Button(
            self.Frame,
            text = 'π',
            command = lambda: self.PiMethod()
            )
        self.PiButton.grid(
            column = 0,
            row = 6,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(6, weight = 3)


        self.eButton = U.ttk.Button(
            self.Frame,
            text = 'e',
            command = lambda: self.eMethod()
            )
        self.eButton.grid(
            column = 1,
            row = 6,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(1, weight = 4)
        self.Frame.rowconfigure(6, weight = 3)


        # ROW SEVEN
        self.ClearAllButton = U.ttk.Button(
            self.Frame,
            text = '<<',
            command = lambda: self.ClearAllMethod()
            )
        self.ClearAllButton.grid(
            column = 0,
            row = 7,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(7, weight = 3)


        self.ClearOneButton = U.ttk.Button(
            self.Frame,
            text = '<',
            command = lambda: self.ClearOneMethod()
            )
        self.ClearOneButton.grid(
            column = 1,
            row = 7,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(1, weight = 4)
        self.Frame.rowconfigure(7, weight = 3)


        # ROW EIGHT
        self.AddButton = U.ttk.Button(
            self.Frame,
            text = '+',
            command = lambda: self.InputCharacter(' + ')
            )
        self.AddButton.grid(
            column = 0,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(8, weight = 3)


        self.SubtractButton = U.ttk.Button(
            self.Frame,
            text = '-',
            command = lambda: self.InputCharacter(' - ')
            )
        self.SubtractButton.grid(
            column = 1,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(1, weight = 4)
        self.Frame.rowconfigure(8, weight = 3)


        self.MultiplyButton = U.ttk.Button(
            self.Frame,
            text = '×',
            command = lambda: self.InputCharacter(' × ')
            )
        self.MultiplyButton.grid(
            column = 2,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.grid_columnconfigure(2, weight = 4)
        self.Frame.grid_rowconfigure(8, weight = 3)


        self.DivideButton = U.ttk.Button(
            self.Frame,
            text = '÷',
            command = lambda: self.InputCharacter(' ÷ ')
            )
        self.DivideButton.grid(
            column = 3,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(3, weight = 4)
        self.Frame.rowconfigure(8, weight = 3)


        self.GetPowerButton = U.ttk.Button(
            self.Frame,
            text = '˄',
            command = lambda: self.InputCharacter(' ˄ ')
            )
        self.GetPowerButton.grid(
            column = 4,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(4, weight = 4)
        self.Frame.rowconfigure(8, weight = 3)


        self.GetRootButton = U.ttk.Button(
            self.Frame,
            text = '˅',
            command = lambda: self.InputCharacter(' ˅ ')
            )
        self.GetRootButton.grid(
            column = 5,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(5, weight = 4)
        self.Frame.rowconfigure(8, weight = 3)


        self.GetExponentButton = U.ttk.Button(
            self.Frame,
            text = 'T',
            command = lambda: self.InputCharacter(' T ')
            )
        self.GetExponentButton.grid(
            column = 6,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(6, weight = 4)
        self.Frame.rowconfigure(8, weight = 3)


        self.LeftParenthesesButton = U.ttk.Button(
            self.Frame,
            text = '(',
            command = lambda: self.InputCharacter('(')
            )
        self.LeftParenthesesButton.grid(
            column = 7,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(7, weight = 4)
        self.Frame.rowconfigure(8, weight = 3)


        self.RightParenthesesButton = U.ttk.Button(
            self.Frame,
            text = ')',
            command = lambda: self.InputCharacter(')')
            )
        self.RightParenthesesButton.grid(
            column = 8,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(8, weight = 4)
        self.Frame.rowconfigure(8, weight = 3)


        self.EqualButton = U.ttk.Button(
            self.Frame,
            text = '=',
            command = lambda: self.EqualMethod()
            )
        self.EqualButton.grid(
            column = 9,
            row = 8,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(9, weight = 4)
        self.Frame.rowconfigure(8, weight = 3)


        # ROW NINE
        self.ZeroButton = U.ttk.Button(
            self.Frame,
            text = '0',
            state = 'normal',
            command = lambda: self.InputCharacter('0')
            )
        self.ZeroButton.grid(
            column = 0,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        self.OneButton = U.ttk.Button(
            self.Frame,
            text = '1',
            state = 'normal',
            command = lambda: self.InputCharacter('1')
            )
        self.OneButton.grid(
            column = 1,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(1, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        self.TwoButton = U.ttk.Button(
            self.Frame,
            text = '2',
            state = 'normal',
            command = lambda: self.InputCharacter('2')
            )
        self.TwoButton.grid(
            column = 2,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(2, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        self.ThreeButton = U.ttk.Button(
            self.Frame,
            text = '3',
            state = 'normal',
            command = lambda: self.InputCharacter('3')
            )
        self.ThreeButton.grid(
            column = 3,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(3, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        self.FourButton = U.ttk.Button(
            self.Frame,
            text = '4',
            state = 'normal',
            command = lambda: self.InputCharacter('4')
            )
        self.FourButton.grid(
            column = 4,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(4, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        self.FiveButton = U.ttk.Button(
            self.Frame,
            text = '5',
            state = 'normal',
            command = lambda: self.InputCharacter('5')
            )
        self.FiveButton.grid(
            column = 5,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(5, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        self.SixButton = U.ttk.Button(
            self.Frame,
            text = '6',
            state = 'normal',
            command = lambda: self.InputCharacter('6')
            )
        self.SixButton.grid(
            column = 6,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(6, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        self.SevenButton = U.ttk.Button(
            self.Frame,
            text = '7',
            state = 'normal',
            command = lambda: self.InputCharacter('7')
            )
        self.SevenButton.grid(
            column = 7,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(7, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        self.EightButton = U.ttk.Button(
            self.Frame,
            text = '8',
            state = 'normal',
            command = lambda: self.InputCharacter('8')
            )
        self.EightButton.grid(
            column = 8,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(8, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        self.NineButton = U.ttk.Button(
            self.Frame,
            text = '9',
            state = 'normal',
            command = lambda: self.InputCharacter('9')
            )
        self.NineButton.grid(
            column = 9,
            row = 9,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(9, weight = 4)
        self.Frame.rowconfigure(9, weight = 3)


        # ROW TEN
        self.TenButton = U.ttk.Button(
            self.Frame,
            text = 'A',
            state = 'disabled',
            command = lambda: self.InputCharacter('A')
            )
        self.TenButton.grid(
            column = 2,
            row = 10,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(2, weight = 4)
        self.Frame.rowconfigure(10, weight = 3)


        self.ElevenButton = U.ttk.Button(
            self.Frame,
            text = 'B',
            state = 'disabled',
            command = lambda: self.InputCharacter('B')
            )
        self.ElevenButton.grid(
            column = 3,
            row = 10,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(3, weight = 4)
        self.Frame.rowconfigure(10, weight = 3)


        self.TwelveButton = U.ttk.Button(
            self.Frame,
            text = 'C',
            state = 'disabled',
            command = lambda: self.InputCharacter('C')
            )
        self.TwelveButton.grid(
            column = 4,
            row = 10,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(4, weight = 4)
        self.Frame.rowconfigure(10, weight = 3)


        self.ThirteenButton = U.ttk.Button(
            self.Frame,
            text = 'D',
            state = 'disabled',
            command = lambda: self.InputCharacter('D')
            )
        self.ThirteenButton.grid(
            column = 5,
            row = 10,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(5, weight = 4)
        self.Frame.rowconfigure(10, weight = 3)


        self.FourteenButton = U.ttk.Button(
            self.Frame,
            text = 'E',
            state = 'disabled',
            command = lambda: self.InputCharacter('E')
            )
        self.FourteenButton.grid(
            column = 6,
            row = 10,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(6, weight = 4)
        self.Frame.rowconfigure(10, weight = 3)


        self.FifteenButton = U.ttk.Button(
            self.Frame,
            text = 'F',
            state = 'disabled',
            command = lambda: self.InputCharacter('F')
            )
        self.FifteenButton.grid(
            column = 7,
            row = 10,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(7, weight = 4)
        self.Frame.rowconfigure(10, weight = 3)


        # ROW ELEVEN
        self.ExpButton = U.ttk.Button(
            self.Frame,
            text = 'Exp',
            command = lambda: self.InputCharacter('e')
            )
        self.ExpButton.grid(
            column = 0,
            row = 11,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(0, weight = 4)
        self.Frame.rowconfigure(11, weight = 3)


        self.PosButton = U.ttk.Button(
            self.Frame,
            text = 'Pos',
            command = lambda: self.InputCharacter('+')
            )
        self.PosButton.grid(
            column = 1,
            row = 11,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(1, weight = 4)
        self.Frame.rowconfigure(11, weight = 3)


        self.NegButton = U.ttk.Button(
            self.Frame,
            text = 'Neg',
            command = lambda: self.InputCharacter('-')
            )
        self.NegButton.grid(
            column = 2,
            row = 11,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(2, weight = 4)
        self.Frame.rowconfigure(11, weight = 3)


        self.PointButton = U.ttk.Button(
            self.Frame,
            text = '.',
            command = lambda: self.InputCharacter('.')
            )
        self.PointButton.grid(
            column = 7,
            row = 11,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(7, weight = 4)
        self.Frame.rowconfigure(11, weight = 3)


        self.ColonButton = U.ttk.Button(
            self.Frame,
            text = ':',
            state = 'disabled',
            command = lambda: self.InputCharacter(':')
            )
        self.ColonButton.grid(
            column = 8,
            row = 11,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(8, weight = 4)
        self.Frame.rowconfigure(11, weight = 3)


        self.BarButton = U.ttk.Button(
            self.Frame,
            text = '|',
            state = 'disabled',
            command = lambda: self.InputCharacter('|')
            )
        self.BarButton.grid(
            column = 9,
            row = 11,
            sticky = 'wens'
            )
        self.Frame.columnconfigure(9, weight = 4)
        self.Frame.rowconfigure(11, weight = 3)


        # VARIABLES
        self.NumberButtonList = [self.ZeroButton, self.OneButton, self.TwoButton, self.ThreeButton,
                                 self.FourButton, self.FiveButton, self.SixButton, self.SevenButton,
                                 self.EightButton, self.NineButton, self.TenButton,
                                 self.ElevenButton, self.TwelveButton, self.ThirteenButton,
                                 self.FourteenButton, self.FifteenButton]

        self.MethodButtonList = [self.BaseButton, self.FractionButton, self.RoundRadixButton,
                                 self.RoundCommonButton, self.RadToRadButton, self.ComToRadButton,
                                 self.RadToComButton, self.ComToComButton, self.SinButton,
                                 self.CosButton, self.TanButton, self.SinAButton, self.CosAButton,
                                 self.TanAButton,
                                 self.PiButton, self.eButton, self.EqualButton, self.AddButton,
                                 self.SubtractButton, self.MultiplyButton, self.DivideButton,
                                 self.GetPowerButton, self.GetRootButton, self.GetExponentButton,
                                 self.LeftParenthesesButton, self.RightParenthesesButton,
                                 self.ExpButton, self.PosButton, self.NegButton]
                                 # Might get rid of SinA, etc. and add radian Sin, etc. ....

        self.FractionButtonList = [self.PointButton, self.ColonButton, self.BarButton]


    # METHODS
    def BaseMethod(self):
        if self.Mode != 'Base':
            self.Mode = 'Base'
            for Element in self.MethodButtonList:
                if Element['text'] != 'Base':
                    Element.configure(state = 'disabled')
            for Element in self.FractionButtonList:
                Element.configure(state = 'disabled')
            UsedDigits = self.NumberButtonList[:10]
            UnusedDigits = self.NumberButtonList[10:]
            for Element in UsedDigits:
                Element.configure(state = 'normal')
            for Element in UnusedDigits:
                Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = (
                'Select one base between --and including-- 2 and 16')
            self.OutputScreen.configure(
                text = self.Output,
                anchor = 'w',
                )
        else:
            if self.Input != '':
                if self.Input in self.AcceptableBases:
                    self.Base = self.Input
                    self.BaseDisplayButton.configure(text = self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                else:
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
            else:
                self.Base = '10'
                self.BaseDisplayButton.configure(text = self.Base)
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def FractionMethod(self):
        if self.Fraction == 'Rad':
            self.Fraction = 'Com'
            self.FractionDisplayButton.configure(text = self.Fraction)
            self.RadToRadButton.configure(state = 'disabled')
            self.ComToRadButton.configure(state = 'disabled')
            self.RadToComButton.configure(state = 'normal')
            self.ComToComButton.configure(state = 'normal')
            self.ExpButton.configure(state = 'disabled')
            self.PosButton.configure(state = 'disabled')
            self.NegButton.configure(state = 'disabled')
            self.PointButton.configure(state = 'disabled')
            self.ColonButton.configure(state = 'normal')
            self.BarButton.configure(state = 'normal')
        else:
            self.Fraction = 'Rad'
            self.FractionDisplayButton.configure(text = self.Fraction)
            self.RadToRadButton.configure(state = 'normal')
            self.ComToRadButton.configure(state = 'normal')
            self.RadToComButton.configure(state = 'disabled')
            self.ComToComButton.configure(state = 'disabled')
            self.ExpButton.configure(state = 'normal')
            self.PosButton.configure(state = 'normal')
            self.NegButton.configure(state = 'normal')
            self.PointButton.configure(state = 'normal')
            self.ColonButton.configure(state = 'disabled')
            self.BarButton.configure(state = 'disabled')
        return


    def RoundRadixMethod(self):
        if self.Mode != 'RoundRadix':
            self.Mode = 'RoundRadix'
            for Element in self.MethodButtonList:
                if Element['text'] != '(R)':
                    Element.configure(state = 'disabled')
            for Element in self.FractionButtonList:
                Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = (
                'Select the number of places after the decimal point that you want to round up to.')
            self.OutputScreen.configure(
                text = self.Output,
                anchor = 'w',
                )
        else:
            if self.Input != '':
                self.RoundRadixStorage[self.Base] = self.Input
                self.RoundRadixDisplayButton.configure(text = self.RoundRadixStorage[self.Base])
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
            else:
                self.RoundRadixStorage[self.Base] = '_'
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def RoundCommonMethod(self):
        if self.Mode != 'RoundCommon':
            self.Mode = 'RoundCommon'
            for Element in self.MethodButtonList:
                if Element['text'] != '(C)':
                    Element.configure(state = 'disabled')
            for Element in self.FractionButtonList:
                Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = 'Select the root denominator.'
            self.OutputScreen.configure(
                text = self.Output,
                anchor = 'w',
                )
        else:
            if self.Input != '':
                if self.RootDenominatorStorage[self.Base] == '_':
                    self.RootDenominatorStorage[self.Base] = self.Input
                    self.RoundCommon = f'{self.RootDenominatorStorage[self.Base]}  {self.PowerDenominatorStorage[self.Base]}'
                    self.RoundCommonDisplayButton.configure(text = self.RoundCommon)
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
                    self.Output = 'Select the power denominator.'
                    self.OutputScreen.configure(text = self.Output)
                else: # self.PowerDenominatorStorage[self.Base] != '_'
                    self.PowerDenominatorStorage[self.Base] = self.Input
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
            else:
                self.RootDenominatorStorage[self.Base] = '_'
                self.PowerDenominatorStorage[self.Base] = '_'
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def RadToRadMethod(self):
        if self.Mode != 'RadToRad':
            self.Mode = 'RadToRad'
            for Element in self.MethodButtonList:
                if Element['text'] != 'R -> R':
                    Element.configure(state = 'disabled')
            UsedDigits = self.Digits[:10]
            for Element in self.NumberButtonList:
                if Element['text'] in UsedDigits:
                    Element.configure(state = 'normal')
                else:
                    Element.configure(state = 'disabled')
            for Element in self.FractionButtonList:
                Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = ('Enter base of radix.')
            self.OutputScreen.configure(
                text = self.Output,
                anchor = 'w',
                )
        else:
            if self.Input != '':
                if self.BaseOfRadix == '':
                    self.BaseOfRadix = self.Input
                    UsedDigits = self.Digits[:int(self.BaseOfRadix)]
                    for Element in self.NumberButtonList:
                        if Element['text'] in UsedDigits:
                            Element.configure(state = 'normal')
                        else:
                            Element.configure(state = 'disabled')
                    self.PointButton.configure(state = 'normal')
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
                    self.Output = 'Enter radix.'
                    self.OutputScreen.configure(text = self.Output)
                else:
                    self.Radix = self.Input
                    self.Radix = I.BaseNRadixToBaseNRadix(self.Radix, self.BaseOfRadix, self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                    self.Input = f'{self.Input}{self.Radix}'
                    self.InputScreen.configure(text = self.Input)
                    self.BaseOfRadix = ''
                    self.Radix = ''
            else:
                self.BaseOfRadix = ''
                self.Radix = ''
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def ComToRadMethod(self):
        if self.Mode != 'ComToRad':
            self.Mode = 'ComToRad'
            for Element in self.MethodButtonList:
                if Element['text'] != 'C -> R':
                    Element.configure(state = 'disabled')
            UsedDigits = self.Digits[:10]
            for Element in self.NumberButtonList:
                if Element['text'] in UsedDigits:
                    Element.configure(state = 'normal')
                else:
                    Element.configure(state = 'disabled')
            for Element in self.FractionButtonList:
                Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = (
                'Enter base of common.')
            self.OutputScreen.configure(
                text = self.Output,
                anchor = 'w',
                )
        else:
            if self.Input != '':
                if self.BaseOfCommon == '':
                    self.BaseOfCommon = self.Input
                    UsedDigits = self.Digits[:int(self.BaseOfCommon)]
                    for Element in self.NumberButtonList:
                        if Element['text'] in UsedDigits:
                            Element.configure(state = 'normal')
                        else:
                            Element.configure(state = 'disabled')
                    self.ColonButton.configure(state = 'normal')
                    self.BarButton.configure(state = 'normal')
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
                    self.Output = 'Enter common.'
                    self.OutputScreen.configure(text = self.Output)
                else:
                    self.Common = self.Input
                    self.Radix = I.BaseNCommonToBaseNRadix(self.Common, self.BaseOfCommon, self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                    self.Input = f'{self.Input}{self.Radix}'
                    self.InputScreen.configure(text = self.Input)
                    self.BaseOfCommon = ''
                    self.Common = ''
                    self.Radix = ''
            else:
                self.BaseOfCommon = ''
                self.Common = ''
                self.Radix = ''
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def RadToComMethod(self):
        if self.Mode != 'RadToCom':
            self.Mode = 'RadToCom'
            for Element in self.MethodButtonList:
                if Element['text'] != 'R -> C':
                    Element.configure(state = 'disabled')
            UsedDigits = self.Digits[:10]
            for Element in self.NumberButtonList:
                if Element['text'] in UsedDigits:
                    Element.configure(state = 'normal')
                else:
                    Element.configure(state = 'disabled')
            for Element in self.FractionButtonList:
                Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = (
                'Enter base of radix.')
            self.OutputScreen.configure(
                text = self.Output,
                anchor = 'w',
                )
        else:
            if self.Input != '':
                if self.BaseOfRadix == '':
                    self.BaseOfRadix = self.Input
                    UsedDigits = self.Digits[:int(self.BaseOfRadix)]
                    for Element in self.NumberButtonList:
                        if Element['text'] in UsedDigits:
                            Element.configure(state = 'normal')
                        else:
                            Element.configure(state = 'disabled')
                    self.PointButton.configure(state = 'normal')
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
                    self.Output = 'Enter radix.'
                    self.OutputScreen.configure(text = self.Output)
                else:
                    self.Radix = self.Input
                    self.Common = I.BaseNRadixToBaseNCommon(self.Radix, self.BaseOfRadix, self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                    self.Input = f'{self.Input}{self.Common}'
                    self.InputScreen.configure(text = self.Input)
                    self.BaseOfRadix = ''
                    self.Radix = ''
                    self.Common = ''
            else:
                self.BaseOfRadix = ''
                self.Radix = ''
                self.Common = ''
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def ComToComMethod(self):
        if self.Mode != 'ComToCom':
            self.Mode = 'ComToCom'
            for Element in self.MethodButtonList:
                if Element['text'] != 'C -> C':
                    Element.configure(state = 'disabled')
            UsedDigits = self.Digits[:10]
            for Element in self.NumberButtonList:
                if Element['text'] in UsedDigits:
                    Element.configure(state = 'normal')
                else:
                    Element.configure(state = 'disabled')
            for Element in self.FractionButtonList:
                Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = (
                'Enter base of common.')
            self.OutputScreen.configure(
                text = self.Output,
                anchor = 'w',
                )
        else:
            if self.Input != '':
                if self.BaseOfCommon == '':
                    self.BaseOfCommon = self.Input
                    UsedDigits = self.Digits[:int(self.BaseOfCommon)]
                    for Element in self.NumberButtonList:
                        if Element['text'] in UsedDigits:
                            Element.configure(state = 'normal')
                        else:
                            Element.configure(state = 'disabled')
                    self.ColonButton.configure(state = 'normal')
                    self.BarButton.configure(state = 'normal')
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
                    self.Output = 'Enter common.'
                    self.OutputScreen.configure(text = self.Output)
                else:
                    self.Common = self.Input
                    self.Common = I.BaseNCommonToBaseNCommon(self.Common, self.BaseOfCommon, self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                    self.Input = f'{self.Input}{self.Common}'
                    self.InputScreen.configure(text = self.Input)
                    self.BaseOfCommon = ''
                    self.Common = ''
            else:
                self.BaseOfCommon = ''
                self.Common = ''
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def OffMethod(self):
        self.Window.destroy()
        return


    def SinMethod(self):
        if self.Mode == 'Calculator':
            self.Mode = 'Sin'
            for Element in self.MethodButtonList:
                if Element['text'] != 'Sin':
                    Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = ('Enter the degree of Sin.')
            self.OutputScreen.configure(text = self.Output)
        else:
            if self.Input != '':
                try:
                    if isinstance(float(self.Input), float):
                        if self.Base != '10':
                            self.Input = I.BaseNRadixToBaseTenRadix(self.Input, self.Base)
                        Radians = U.math.radians(float(self.Input))
                        Ratio = U.math.sin(Radians)
                        if self.Base != '10':
                            Ratio = I.BaseTenRadixToBaseNRadix(Ratio, self.Base)
                        self.Mode = 'Calculator'
                        self.RetrieveAndDisplay()
                        self.Input += str(Ratio)
                        self.InputScreen.configure(text = self.Input)
                except:
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
            else:
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def CosMethod(self):
        if self.Mode == 'Calculator':
            self.Mode = 'Cos'
            for Element in self.MethodButtonList:
                if Element['text'] != 'Cos':
                    Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = ('Enter the degree of Cos.')
            self.OutputScreen.configure(text = self.Output)
        else:
            if self.Input != '':
                try:
                    if self.Base != '10':
                        self.Input = I.BaseNRadixToBaseTenRadix(self.Input, self.Base)
                    Radians = U.math.radians(float(self.Input))
                    Ratio = U.math.cos(Radians)
                    if self.Base != '10':
                        Ratio = I.BaseTenRadixToBaseNRadix(Ratio, self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                    self.Input += str(Ratio)
                    self.InputScreen.configure(text = self.Input)
                except:
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
            else:
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def TanMethod(self):
        if self.Mode == 'Calculator':
            self.Mode = 'Tan'
            for Element in self.MethodButtonList:
                if Element['text'] != 'Tan':
                    Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = ('Enter the degree of Tan.')
            self.OutputScreen.configure(text = self.Output)
        else:
            if self.Input != '':
                try:
                    if self.Base != '10':
                        self.Input = I.BaseNRadixToBaseTenRadix(self.Input, self.Base)
                    Radians = U.math.radians(float(self.Input))
                    Ratio = U.math.tan(Radians)
                    if self.Base != '10':
                        Ratio = I.BaseTenRadixToBaseNRadix(Ratio, self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                    self.Input += str(Ratio)
                    self.InputScreen.configure(text = self.Input)
                except:
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
            else:
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def SinAMethod(self):
        if self.Mode == 'Calculator':
            self.Mode = 'SinA'
            for Element in self.MethodButtonList:
                if Element['text'] != 'SinA':
                    Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = ('Enter the degree of SinA.')
            self.OutputScreen.configure(text = self.Output)
        else:
            if self.Input != '':
                try:
                    if self.Base != '10':
                        self.Input = I.BaseNRadixToBaseTenRadix(self.Input, self.Base)
                    Radians = U.math.asin(float(self.Input))
                    Degrees = U.math.degrees(Radians)
                    if self.Base != '10':
                        Degrees = I.BaseTenRadixToBaseNRadix(Degrees, self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                    self.Input += str(Degrees)
                    self.InputScreen.configure(text = self.Input)
                except:
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
            else:
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def CosAMethod(self):
        if self.Mode == 'Calculator':
            self.Mode = 'CosA'
            for Element in self.MethodButtonList:
                if Element['text'] != 'CosA':
                    Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = ('Enter the degree of CosA.')
            self.OutputScreen.configure(text = self.Output)
        else:
            if self.Input != '':
                try:
                    if self.Base != '10':
                        self.Input = I.BaseNRadixToBaseTenRadix(self.Input, self.Base)
                    Radians = U.math.acos(float(self.Input))
                    Degrees = U.math.degrees(Radians)
                    if self.Base != '10':
                        Degrees = I.BaseTenRadixToBaseNRadix(Degrees, self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                    self.Input += str(Degrees)
                    self.InputScreen.configure(text = self.Input)
                except:
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
            else:
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def TanAMethod(self):
        if self.Mode == 'Calculator':
            self.Mode = 'TanA'
            for Element in self.MethodButtonList:
                if Element['text'] != 'TanA':
                    Element.configure(state = 'disabled')
            self.StoreAndClear()
            self.Output = ('Enter the degree of TanA.')
            self.OutputScreen.configure(text = self.Output)
        else:
            if self.Input != '':
                try:
                    if self.Base != '10':
                        self.Input = I.BaseNRadixToBaseTenRadix(self.Input, self.Base)
                    Radians = U.math.atan(float(self.Input))
                    Degrees = U.math.degrees(Radians)
                    if self.Base != '10':
                        Degrees = I.BaseTenRadixToBaseNRadix(Degrees, self.Base)
                    self.Mode = 'Calculator'
                    self.RetrieveAndDisplay()
                    self.Input += str(Degrees)
                    self.InputScreen.configure(text = self.Input)
                except:
                    self.Input = ''
                    self.InputScreen.configure(text = self.Input)
            else:
                self.Mode = 'Calculator'
                self.RetrieveAndDisplay()
        return


    def PiMethod(self):
        Pi = U.math.pi
        if self.Base != '10':
            Pi = I.BaseTenRadixToBaseNRadix(Pi, self.Base)
            Pi = I.FormatNumber(Pi)
        else:
            Pi = str(Pi)
        self.Input += Pi
        self.InputScreen.configure(text = self.Input)
        return


    def eMethod(self):
        e = U.math.e
        if self.Base != '10':
            e = I.BaseTenRadixToBaseNRadix(e, self.Base)
            e = I.FormatNumber(e)
        else:
            e = str(e)
        self.Input += e
        self.InputScreen.configure(text = self.Input)
        return


    def ClearAllMethod(self):
        self.Input = ''
        self.Output = ''
        self.InputScreen.configure(text = self.Input)
        self.OutputScreen.configure(text = self.Output)
        return


    def ClearOneMethod(self):
        if len(self.Input) > 0:
            if self.Input[-1] == ' ':
                self.Input = self.Input[:-3]
            else:
                self.Input = self.Input[:-1]
            self.InputScreen.configure(text = self.Input)
        return


    def EqualMethod(self):
        ExpressionList = I.ParseExpression(self.Input, self.Fraction, self.Base)
        Result = I.Calculate(ExpressionList)
        if 'e' in Result:
            Result = I.EFormatToRadix(Result, '10')
        if self.Base != '10':
            Result = I.BaseTenRadixToBaseNRadix(Result, self.Base)
        if self.Fraction == 'Rad':
            if self.RoundRadixStorage[self.Base] != '_':
                Result = I.RoundRadix(Result, self.Base, self.RoundRadixStorage[self.Base])
            Result = I.RadixToEFormat(Result, self.Base)
            if 'e' not in Result:
                Result = I.FormatNumber(Result)
        else: # self.Fraction == 'Com'
            Result = I.RadixToCommon(Result, self.Base)
            if self.RoundCommon != '_  _':
                Result = I.RoundCommon(Result, self.Base, self.RootDenominatorStorage[self.Base], self.PowerDenominatorStorage[self.Base])
            Result = I.FormatNumber(Result)
        self.Output = Result
        self.OutputScreen.configure(text = self.Output)
        return


    def InputCharacter(self, Character):
        self.Input = f'{self.Input}{Character}'
        DigitsAndLike = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
                         'E', 'F', '.', ':', '|', '+', '-']
        Separators = [',', '_']
        WorkingNumber = ''
        Count = 0
        for Element in reversed(self.Input):
            if Element in DigitsAndLike:
                WorkingNumber = f'{WorkingNumber}{Element}'
                Count += 1
            elif Element in Separators:
                Count += 1
            else:
                break
        if 'e' not in WorkingNumber:
            if Count > 0:
                OldNumber = ''
                for Element in reversed(WorkingNumber):
                    OldNumber = f'{OldNumber}{Element}'
                self.Input = self.Input[:-Count]
                NewNumber = I.FormatNumber(OldNumber)
                self.Input = f'{self.Input}{NewNumber}'
                self.InputScreen.configure(text = self.Input)
            else:
                self.InputScreen.configure(text = self.Input)
        return


    def StoreAndClear(self):
        self.InputStorage[self.Base] = self.Input
        self.Input = ''
        self.InputScreen.configure(text = self.Input)
        self.OutputStorage[self.Base] = self.Output
        self.Output = ''
        self.OutputScreen.configure(text = self.Output)
        return


    def RetrieveAndDisplay(self):
        self.Input = self.InputStorage[self.Base]
        self.InputScreen.configure(text = self.Input)
        self.Output = self.OutputStorage[self.Base]
        self.OutputScreen.configure(
            text = self.Output,
            anchor = 'e',
            )
        self.RoundRadixDisplayButton.configure(text = self.RoundRadixStorage[self.Base])
        self.RoundCommon = f'{self.RootDenominatorStorage[self.Base]}  {self.PowerDenominatorStorage[self.Base]}'
        self.RoundCommonDisplayButton.configure(text = self.RoundCommon)
        for Element in self.MethodButtonList:
            Element.configure(state = 'normal')
        if self.Fraction == 'Rad':
            self.RadToRadButton.configure(state = 'normal')
            self.ComToRadButton.configure(state = 'normal')
            self.RadToComButton.configure(state = 'disabled')
            self.ComToComButton.configure(state = 'disabled')
            self.ExpButton.configure(state = 'normal')
            self.PosButton.configure(state = 'normal')
            self.NegButton.configure(state = 'normal')
            self.PointButton.configure(state = 'normal')
            self.ColonButton.configure(state = 'disabled')
            self.BarButton.configure(state = 'disabled')
        else:
            self.RadToRadButton.configure(state = 'disabled')
            self.ComToRadButton.configure(state = 'disabled')
            self.RadToComButton.configure(state = 'normal')
            self.ComToComButton.configure(state = 'normal')
            self.ExpButton.configure(state = 'disabled')
            self.PosButton.configure(state = 'disabled')
            self.NegButton.configure(state = 'disabled')
            self.PointButton.configure(state = 'disabled')
            self.ColonButton.configure(state = 'normal')
            self.BarButton.configure(state = 'normal')
        UsedDigits = self.Digits[:int(self.Base)]
        for Element in self.NumberButtonList:
            if Element['text'] in UsedDigits:
                Element.configure(state = 'normal')
            else:
                Element.configure(state = 'disabled')
        return


    def ResizeFont(self, Event):
        Width = self.Window.winfo_width()
        Height = self.Window.winfo_height()
        Diagonal = U.math.sqrt(Width ** 2 + (Height ** 2))
        Size = str(int(Diagonal / self.BaseDiagonal * self.BaseFontSize))
        self.FontSize = U.font.Font(size = Size)
        self.InputScreen.configure(font = self.FontSize)
        self.OutputScreen.configure(font = self.FontSize)
        self.Style.configure('TButton', font = self.FontSize)
        return


    def Mainloop(self):
        self.Window.mainloop()
        return


if __name__ == '__main__':
    import builtins
    # U Modules:
    import tkinter as Tk
    from tkinter import ttk
    from tkinter import font
    import math
    # I Module:
    from Module import I
    class U():
        Tk = Tk
        ttk = ttk
        font = font
        math = math
    builtins.U = U
    builtins.I = I
    Calculator = I.Calculator()
    Calculator.Mainloop()

# Python 3.9.0

# BaseNCommonToBaseNCommon

def BaseNCommonToBaseNCommon(Common, FromBase, ToBase):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    FromBase: must be a string integer that's one number between and including 2 and 16.
    ToBase: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    Common
    CommonToRadix
    BaseNRadixToBaseTenRadix
    BaseTenRadixToBaseNRadix
    RadixToCommon
    FormatNumber
    '''


    Common = I.Common(Common)
    Separators = [',', '_']
    WorkingCommon = ''
    for Element in Common:
        if Element in Separators:
            continue
        else:
            WorkingCommon = f'{WorkingCommon}{Element}'
    Common = WorkingCommon
    Radix = I.CommonToRadix(Common, FromBase)
    if FromBase != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, FromBase)
    if ToBase != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, ToBase)
    Common = I.RadixToCommon(Radix, ToBase)
    Common = I.FormatNumber(Common)
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base N Common To Base N Common')
        print()
        Common = input('Enter Common: ')
        FromBase = input('Enter FromBase: ')
        ToBase = input('Enter ToBase: ')
        print()
        Common = I.BaseNCommonToBaseNCommon(Common, FromBase, ToBase)
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# BaseNRadixToBaseTenRadix

def BaseNRadixToBaseTenRadix(Radix, Base):


    '''
    Parameters:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseNIntegerToBaseTenInteger
    '''


    AlternativeDigits = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
        }
    RadixList = []
    for Element in Radix:
        if Element in AlternativeDigits:
            RadixList.append(AlternativeDigits[Element])
        else:
            RadixList.append(Element)
    IndexOfPoint = RadixList.index('.')
    Whole = RadixList[:IndexOfPoint]
    Fraction = RadixList[(IndexOfPoint + 1):]
    # Whole part.
    PositiveMagnitudes = []
    for Exponent in range(len(Whole)):
        Magnitude = int(Base) ** Exponent
        PositiveMagnitudes.append(Magnitude)
    PositiveMagnitudes.reverse()
    WorkingWhole = 0
    for Index in range(len(PositiveMagnitudes)):
        WorkingWhole += (float(Whole[Index]) * PositiveMagnitudes[Index])
    Whole = int(WorkingWhole)
    # Fraction part
    Denominator = '1'
    for Times in range(len(Fraction)):
        Denominator = f'{Denominator}0'
    Numerator = I.BaseNIntegerToBaseTenInteger(Fraction, Base)
    Denominator = I.BaseNIntegerToBaseTenInteger(Denominator, Base)
    Fraction = str(int(Numerator) / int(Denominator))
    Fraction = Fraction[2:]
    # Whole and Fraction parts
    Radix = f'{Whole}.{Fraction}'
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base N Radix To Base Ten Radix')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        print()
        Radix = I.BaseNRadixToBaseTenRadix(Radix, Base)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# BaseNIntegerToBaseTenInteger

def BaseNIntegerToBaseTenInteger(Integer, Base):


    '''
    Parameters:
    Integer: must be a string integer that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    '''


    AlternativeDigits = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
        }
    IntegerList = []
    for Element in Integer:
        if Element in AlternativeDigits:
            IntegerList.append(AlternativeDigits[Element])
        else:
            IntegerList.append(Element)
    PositiveMagnitudes = []
    for Exponent in range(len(IntegerList)):
        Magnitude = int(Base) ** Exponent
        PositiveMagnitudes.append(Magnitude)
    PositiveMagnitudes.reverse()
    Integer = 0
    for Index in range(len(PositiveMagnitudes)):
        Integer += (int(IntegerList[Index]) * PositiveMagnitudes[Index])
    return str(Integer)


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base N Integer To Base Ten Integer')
        print()
        Integer = input('Enter Integer: ')
        Base = input('Enter Base: ')
        print()
        Integer = I.BaseNIntegerToBaseTenInteger(Integer, Base)
        print(Integer)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# BaseTenRadixToBaseNRadix

def BaseTenRadixToBaseNRadix(Radix, Base):


    '''
    Parameters:
    Radix: must be a string radix that's in base 10.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    GetExponent
    SimplifyRoundedCommon
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    Whole = int(Whole)
    Base = int(Base)
    if Whole != 0:
        Exponent = 1
        Magnitude = Base ** Exponent
        while Whole > Magnitude:
            Exponent = Exponent + 1
            Magnitude = Base ** Exponent
        if Magnitude > Whole:
            Magnitude = Magnitude / Base
            Exponent = Exponent - 1
        Digits = []
        Digit = Whole // Magnitude
        Remainder = Whole - (Digit * Magnitude)
        Digits.append(int(Digit))
        if Exponent != 0:
            Magnitude = Magnitude / Base
            Exponent = Exponent - 1
            if Remainder >= Base:
                GoodToGo = 'no'
                while GoodToGo == 'no':
                    if Magnitude > Remainder:
                        Digits.append(0)
                        Magnitude = Magnitude / Base
                        Exponent = Exponent - 1
                    else: # Magnitude < Remainder
                        Digit = Remainder // Magnitude
                        Remainder = Remainder - (Digit * Magnitude)
                        Digits.append(int(Digit))
                        Magnitude = Magnitude / Base
                        Exponent = Exponent - 1
                    if Remainder >= Base:
                        GoodToGo = 'no'
                    else:
                        GoodToGo = 'yes'
            if Exponent != 0:
                for Count in range(Exponent):
                    Digits.append(0)
            Digits.append(int(Remainder))
        AlternativeDigits = {
            '10': 'A',
            '11': 'B',
            '12': 'C',
            '13': 'D',
            '14': 'E',
            '15': 'F'
            }
        Whole = ''
        for Digit in Digits:
            if str(Digit) in AlternativeDigits:
                Whole = f'{Whole}{AlternativeDigits[str(Digit)]}'
            else:
                Whole = f'{Whole}{Digit}'
    #Fraction part
    if Fraction != '0':
        RootDenominator = int(Base)
        PowerDenominator = int(Base) ** 16
        Exponent = I.GetExponent(RootDenominator, PowerDenominator)
        Denominators = [RootDenominator]
        WorkingPowerDenominator = RootDenominator
        for Times in range(Exponent - 1):
            WorkingPowerDenominator *= RootDenominator
            Denominators.append(WorkingPowerDenominator)
        Denominator = PowerDenominator
        Numerator = float(f'.{Fraction}') * Denominator
        if Numerator % 1 == 0:
            if Numerator in Denominators:
                Denominator /= Numerator
                Numerator /= Numerator
        else:
            Numerator = round(Numerator)
            if Numerator in Denominators:
                Denominator /= Numerator
                Numerator /= Numerator
        Numerator = int(Numerator)
        Denominator = int(Denominator)
        Common = f'0:{Numerator}|{Denominator}'
        Common = I.SimplifyRoundedCommon(Common, '10', Base)
        IndexOfColon = Common.index(':')
        IndexOfBar = Common.index('|')
        Numerator = Common[(IndexOfColon + 1):IndexOfBar]
        Denominator = Common[(IndexOfBar + 1):]
        Numerator = I.BaseTenIntegerToBaseNInteger(Numerator, Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(Denominator, Base)
        Fraction = Numerator
        for Times in range((len(Denominator) - 1 - len(Numerator))):
            Fraction = f'0{Fraction}'
    Radix = f'{Whole}.{Fraction}'
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base Ten Radix To Base N Radix')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        print()
        Radix = I.BaseTenRadixToBaseNRadix(Radix, Base)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# BaseTenIntegerToBaseNInteger

def BaseTenIntegerToBaseNInteger(Integer, Base):


    '''
    Parameters:
    Integer: must be a string integer that's in base 10.
    Base: must be a string integer that's one number between and including 2 and 16.
    '''


    Integer = int(Integer)
    Base = int(Base)
    Exponent = 1
    Magnitude = Base ** Exponent
    while Integer > Magnitude:
        Exponent = Exponent + 1
        Magnitude = Base ** Exponent
    if Magnitude > Integer:
        Magnitude = Magnitude / Base
        Exponent = Exponent - 1
    Digits = []
    Digit = int(Integer // Magnitude)
    Remainder = Integer - (Digit * Magnitude)
    Digits.append(Digit)
    if Exponent != 0:
        Magnitude = Magnitude / Base
        Exponent = Exponent - 1
        if Remainder >= Base:
            GoodToGo = 'No'
            while GoodToGo == 'No':
                if Magnitude > Remainder:
                    Digits.append(0)
                    Magnitude = Magnitude / Base
                    Exponent = Exponent - 1
                else: # Magnitude < Remainder
                    Digit = Remainder // Magnitude
                    Remainder = Remainder - (Digit * Magnitude)
                    Digits.append(int(Digit))
                    Magnitude = Magnitude / Base
                    Exponent = Exponent - 1
                if Remainder >= Base:
                    GoodToGo = 'No'
                else:
                    GoodToGo = 'Yes'
        if Exponent != 0:
            for Count in range(Exponent):
                Digits.append(0)
        Digits.append(int(Remainder))
    AlternativeDigits = {
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
        }
    Integer = ''
    for Digit in Digits:
        if str(Digit) in AlternativeDigits:
            Integer = f'{Integer}{AlternativeDigits[Digit]}'
        else:
            Integer = f'{Integer}{Digit}'
    return Integer


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base Ten Integer To Base N Integer')
        print()
        Integer = input('Enter Integer: ')
        Base = input('Enter Base: ')
        print()
        Integer = I.BaseTenIntegerToBaseNInteger(Integer, Base)
        print(Integer)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# GetExponent

def GetExponent(Root, Power):


    '''
    Parameters:
    Power: must be a literal integer or float.
    Root: must be a literal integer or float.
    '''


    Exponent = 1
    while Power != Root:
        Power = Power / Root
        Exponent += 1
    return Exponent


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Get Exponent')
        print()
        Root = float(input('Enter Root: '))
        Power = float(input('Enter Power: '))
        print()
        Exponent = I.GetExponent(Root, Power)
        print(Exponent)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# SimplifyRoundedCommon

def SimplifyRoundedCommon(Common, Base, Divisor):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') with a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    Divisor: must be a string integer.

    Dependencies:
    Programmer's:
    BaseNIntegerToBaseTenInteger
    BaseTenIntegerToBaseNInteger
    '''


    IndexOfColon = Common.index(':')
    Whole = Common[:IndexOfColon]
    Fraction = Common[(IndexOfColon + 1):]
    IndexOfBar = Fraction.index('|')
    Numerator = Fraction[:IndexOfBar]
    Denominator = Fraction[(IndexOfBar + 1):]
    if Base != '10':
        Whole = I.BaseNIntegerToBaseTenInteger(Whole, Base)
        Numerator = I.BaseNIntegerToBaseTenInteger(Numerator, Base)
        Denominator = I.BaseNIntegerToBaseTenInteger(Denominator, Base)
    Whole = int(Whole)
    Numerator = int(Numerator)
    Denominator = int(Denominator)
    Divisor = int(Divisor)
    GoodToGo = 'No'
    while GoodToGo == 'No':
        if Divisor <= Numerator:
            if Numerator % Divisor == 0 and Denominator % Divisor == 0:
                Numerator /= Divisor
                Denominator /= Divisor
            else:
                GoodToGo = 'Yes'
        else:
            GoodToGo = 'Yes'
    if Base != '10':
        Whole = I.BaseTenIntegerToBaseNInteger(Whole, Base)
        Numerator = I.BaseTenIntegerToBaseNInteger(Numerator, Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(Denominator, Base)
    else:
        Whole = int(Whole)
        Numerator = int(Numerator)
        Denominator = int(Denominator)
    Common = f'{Whole}:{Numerator}|{Denominator}'
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Simplify Rounded Common')
        print()
        Common = input('Enter Common: ')
        Base = input('Enter Base: ')
        Divisor = input('Enter Divisor: ')
        print()
        Common = I.SimplifyRoundedCommon(Common, Base, Divisor)
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

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

# Python 3.9.0

# CommonToRadix

def CommonToRadix(Common, Base):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseNIntegerToBaseTenInteger,
    BaseTenRadixToBaseNRadix
    '''


    IndexOfColon = Common.index(':')
    Whole = Common[:IndexOfColon]
    Fraction = Common[(IndexOfColon + 1):]
    IndexOfBar = Fraction.index('|')
    Numerator = Fraction[:IndexOfBar]
    Denominator = Fraction[(IndexOfBar + 1):]
    if Base != '10':
        Whole = I.BaseNIntegerToBaseTenInteger(Whole, Base)
        Numerator = I.BaseNIntegerToBaseTenInteger(Numerator, Base)
        Denominator = I.BaseNIntegerToBaseTenInteger(Denominator, Base)
    if Numerator == '0' and Denominator == '0':
        Fraction = 0.0
    else:
        Fraction = int(Numerator) / int(Denominator)
    Radix = str(int(Whole) + Fraction)
    if Base != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, Base)
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Common To Radix')
        print()
        Common = input('Enter Common: ')
        Base = input('Enter Base: ')
        print()
        Radix = I.CommonToRadix(Common, Base)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

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
        print()
        Number = I.FormatNumber(Number)
        print(Number)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# RadixToCommon

def RadixToCommon(Radix, Base):


    '''
    Parameters:
    Radix: must be a string radix with a base that's between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseNRadixToBaseTenRadix,
    RoundUpOrTruncate
    BaseTenIntegerToBaseNInteger
    SimplifyCommon
    '''


    if Base != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, Base)
    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[IndexOfPoint:]
    Denominator = 2
    GoodToGo = 'No'
    while GoodToGo == 'No':
        Numerator = float(Fraction) * Denominator
        if Numerator % 1 == 0:
            GoodToGo = 'Yes'
        else:
            Numerator = I.RoundUpOrTruncate(Numerator)
            if Numerator % 1 == 0:
                GoodToGo = 'Yes'
            else:
                Denominator += 1
    if Base != '10':
        Whole = I.BaseTenIntegerToBaseNInteger(Whole, Base)
        Numerator = I.BaseTenIntegerToBaseNInteger(str(int(Numerator)), Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(str(Denominator), Base)
    Whole = int(Whole)
    Numerator = int(Numerator)
    Denominator = int(Denominator)
    if Numerator == 0:
        Denominator = 0
        Common = f'{Whole}:{Numerator}|{Denominator}'
    else:
        Common = f'{Whole}:{Numerator}|{Denominator}'
        Common = I.SimplifyCommon(Common, Base)
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('RadixToCommon')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        print()
        Common = I.RadixToCommon(Radix, Base)
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# RoundUpOrTruncate

def RoundUpOrTruncate(Radix):


    '''
    Parameters:
    Radix: must be a literal float.

    Dependencies:
    Programmer's:
    EFormatToRadix
    '''


    Radix = str(Radix)
    if 'e' in Radix:
        Radix = I.EFormatToRadix(Radix, Base)
    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    LengthOfFraction = len(Fraction)
    Count = 0
    for Digit in Fraction:
        if Digit == '0':
            Count += 1
        else:
            break
    if Count >= 4:
        if Count == LengthOfFraction or Count == (LengthOfFraction - 1):
            Radix = float(Whole)
            return Radix
    else:
        Count = 0
    for Element in Fraction:
        if Element == '9':
            Count += 1
        else:
            break
    if Count >= 4:
        if Count == LengthOfFraction or Count == (LengthOfFraction - 1):
            Radix = float(Whole) + 1
            return Radix
    return float(Radix)


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Round Up Or Truncate')
        print()
        Radix = input('Enter Radix: ')
        print()
        Radix = I.RoundUpOrTruncate(Radix)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# EFormatToRadix

def EFormatToRadix(EFormat, Base):


    '''
    Parameters:
    EFormat: must be a string EFormat ('ne[+/-]n') that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Modules:
    Programmer's:
    BaseNIntegerToBaseTenInteger
    '''


    IndexOfE = EFormat.index('e')
    Radix = EFormat[:IndexOfE]
    Sign = EFormat[(IndexOfE + 1)]
    Exponent = EFormat[(IndexOfE + 2):]
    if '.' in Radix:
        Radix = f'{Radix[0]}{Radix[2:]}'
    if Base != '10':
        Exponent = I.BaseNIntegerToBaseTenInteger(Exponent, Base)
    if Sign == '+':
        Zeros = int(Exponent) - (len(Radix) - 1)
        for Zero in range(Zeros):
            Radix = f'{Radix}0'
        Radix = f'{Radix}.0'
    else: # Sign == '-'
        for Zero in range(int(Exponent) - 1):
            Radix = f'0{Radix}'
        Radix = f'0.{Radix}'
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('EFormatToRadix')
        print()
        EFormat = input('Enter EFormat: ')
        Base = input('Enter Base: ')
        print()
        Radix = I.EFormatToRadix(EFormat, Base)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# SimplifyCommon

def SimplifyCommon(Common, Base):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') with a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseNIntegerToBaseTenInteger
    BaseTenIntegerToBaseNInteger
    '''


    IndexOfColon = Common.index(':')
    Whole = Common[:IndexOfColon]
    Fraction = Common[(IndexOfColon + 1):]
    IndexOfBar = Fraction.index('|')
    Numerator = Fraction[:IndexOfBar]
    Denominator = Fraction[(IndexOfBar + 1):]
    if Base != '10':
        Whole = I.BaseNIntegerToBaseTenInteger(Whole, Base)
        Numerator = I.BaseNIntegerToBaseTenInteger(Numerator, Base)
        Denominator = I.BaseNIntegerToBaseTenInteger(Denominator, Base)
    Whole = int(Whole)
    Numerator = int(Numerator)
    Denominator = int(Denominator)
    Divisor = 2
    GoodToGo = 'No'
    while GoodToGo == 'No':
        if Divisor <= Numerator:
            if Numerator % Divisor == 0 and Denominator % Divisor == 0:
                Numerator /= Divisor
                Denominator /= Divisor
            else:
                Divisor += 1
        else:
            GoodToGo = 'Yes'
    if Base != '10':
        Whole = I.BaseTenIntegerToBaseNInteger(Whole, Base)
        Numerator = I.BaseTenIntegerToBaseNInteger(Numerator, Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(Denominator, Base)
    else:
        Whole = int(Whole)
        Numerator = int(Numerator)
        Denominator = int(Denominator)
    Common = f'{Whole}:{Numerator}|{Denominator}'
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Simplify Common')
        print()
        Common = input('Enter Common: ')
        Base = input('Enter Base: ')
        print()
        Common = I.SimplifyCommon(Common, Base)
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# BaseNCommonToBaseNRadix

def BaseNCommonToBaseNRadix(Common, FromBase, ToBase):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    FromBase: must be a string integer that's one number between and including 2 and 16.
    ToBase: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    Common
    CommonToRadix
    BaseNRadixToBaseTenRadix
    FormatNumber
    '''


    Common = I.Common(Common)
    Separators = [',', '_']
    WorkingCommon = ''
    for Element in Common:
        if Element in Separators:
            continue
        else:
            WorkingCommon = f'{WorkingCommon}{Element}'
    Common = WorkingCommon
    Radix = I.CommonToRadix(Common, FromBase)
    if FromBase != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, FromBase)
    if ToBase != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, ToBase)
    Radix = I.FormatNumber(Radix)
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base N Common To Base N Radix')
        print()
        Common = input('Enter Common: ')
        FromBase = input('Enter FromBase: ')
        ToBase = input('Enter ToBase: ')
        print()
        Common = I.BaseNCommonToBaseNRadix(Common, FromBase, ToBase)
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# BaseNRadixToBaseNCommon

def BaseNRadixToBaseNCommon(Radix, FromBase, ToBase):


    '''
    Parameters:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    FromBase: must be a string integer that's one number between and including 2 and 16.
    ToBase: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    Radix
    BaseNRadixToBaseTenRadix
    RadixToCommon
    FormatNumber
    '''


    Radix = I.Radix(Radix)
    Separators = [',', '_']
    WorkingRadix = ''
    for Element in Radix:
        if Element in Separators:
            continue
        else:
            WorkingRadix = f'{WorkingRadix}{Element}'
    Radix = WorkingRadix
    if FromBase != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, FromBase)
    if ToBase != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, ToBase)
    Common = I.RadixToCommon(Radix, ToBase)
    Common = I.FormatNumber(Common)
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base N Radix To Base N Common')
        print()
        Radix = input('Enter Radix: ')
        FromBase = input('Enter FromBase: ')
        ToBase = input('Enter ToBase: ')
        print()
        Common = I.BaseNRadixToBaseNCommon(Radix, FromBase, ToBase)
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# Radix

def Radix(Radix):


    '''
    Parameters:
    Radix: must be a string radix ('n', 'n.n')
    '''


    if '.' not in Radix:
        Radix = f'{Radix}.0'
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Radix')
        print()
        Radix = input('Enter Radix: ')
        print()
        Radix = I.Radix(Radix)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# BaseNRadixToBaseNRadix

def BaseNRadixToBaseNRadix(Radix, FromBase, ToBase):


    '''
    Parameters:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    FromBase: must be a string integer that's one number between and including 2 and 16.
    ToBase: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    Radix
    BaseNRadixToBaseTenRadix
    BaseTenRadixToBaseNRadix
    FormatNumber
    '''


    Radix = I.Radix(Radix)
    Separators = [',', '_']
    WorkingRadix = ''
    for Element in Radix:
        if Element in Separators:
            continue
        else:
            WorkingRadix = f'{WorkingRadix}{Element}'
    Radix = WorkingRadix
    if FromBase != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, FromBase)
    if ToBase != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, ToBase)
    Radix = I.FormatNumber(Radix)
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Base N Radix To Base N Radix')
        print()
        Radix = input('Enter Radix: ')
        FromBase = input('Enter FromBase: ')
        ToBase = input('Enter ToBase: ')
        print()
        Radix = I.BaseNRadixToBaseNRadix(Radix, FromBase, ToBase)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

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
        print()
        ExpressionList = I.ParseExpression(Expression, Fraction, Base)
        print(ExpressionList)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# RadixToEFormat

def RadixToEFormat(Radix, Base):


    '''
    Parameters:
    Radix: must be a string Radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Dependencies:
    Programmer's:
    BaseTenIntegerToBaseNInteger
    FormatNumber
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    if Whole == '0':
        Zeros = 0
        for Digit in Fraction:
            if Digit == '0':
                Zeros += 1
            else:
                break
        if Zeros >= 4:
            Exponent = Zeros + 1
            if (len(Fraction) - Zeros) > 1:
                Fraction = f'{Fraction[Zeros]}.{Fraction[(Zeros + 1):]}'
            else:
                Fraction = Fraction[Zeros]
            if Base != '10':
                Exponent = I.BaseTenIntegerToBaseNInteger(Exponent, Base)
            Fraction = I.FormatNumber(Fraction)
            EFormat = f'{Fraction}e-{Exponent}'
            return EFormat
    else: # Whole != '0'
        if Fraction == '0':
            Zeros = 0
            for Digit in reversed(Whole):
                if Digit == '0':
                    Zeros += 1
                else:
                    break
            if Zeros >= 4:
                Exponent = len(Whole) - 1
                if (len(Whole) - Zeros) > 1:
                    Whole = f'{Whole[0]}.{Whole[1:-Zeros]}'
                else:
                    Whole = Whole[0]
                if Base != '10':
                    Exponent = I.BaseTenIntegerToBaseNInteger(Exponent, Base)
                Whole = I.FormatNumber(Whole)
                EFormat = f'{Whole}e+{Exponent}'
                return EFormat
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('RadixToEFormat')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        print()
        EFormat = I.RadixToEFormat(Radix, Base)
        print(EFormat)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# RoundCommon

def RoundCommon(Common, Base, RootDenominator, PowerDenominator):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    RootDenominator: must be a string integer.
    PowerDenominator: must be a string integer.

    Dependencies:
    Programmer's:
    CommonToRadix
    BaseNRadixToBaseTenRadix
    GetExponent
    SimplifyRoundedCommon
    '''


    Radix = I.CommonToRadix(Common, Base)
    WorkingRootDenominator = ''
    for Element in RootDenominator:
        if Element != ',':
            WorkingRootDenominator = f'{WorkingRootDenominator}{Element}'
    RootDenominator = WorkingRootDenominator
    WorkingPowerDenominator = ''
    for Element in PowerDenominator:
        if Element != ',':
            WorkingPowerDenominator = f'{WorkingPowerDenominator}{Element}'
    PowerDenominator = WorkingPowerDenominator
    if Base != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, Base)
        RootDenominator = I.BaseNIntegerToBaseTenInteger(RootDenominator, Base)
        PowerDenominator = I.BaseNIntegerToBaseTenInteger(PowerDenominator, Base)
    RootDenominator = int(RootDenominator)
    PowerDenominator = int(PowerDenominator)
    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[IndexOfPoint:]
    Exponent = I.GetExponent(RootDenominator, PowerDenominator)
    Denominators = [RootDenominator]
    WorkingPowerDenominator = RootDenominator
    for Times in range(Exponent - 1):
        WorkingPowerDenominator *= RootDenominator
        Denominators.append(WorkingPowerDenominator)
    Denominator = PowerDenominator
    Numerator = float(Fraction) * Denominator
    if Numerator % 1 == 0:
        if Numerator in Denominators:
            Denominator /= Numerator
            Numerator /= Numerator
    else:
        Numerator = round(Numerator)
        if Numerator in Denominators:
            Denominator /= Numerator
            Numerator /= Numerator
    if Base != '10':
        Whole = I.BaseTenIntegerToBaseNInteger(Whole, Base)
        Numerator = I.BaseTenIntegerToBaseNInteger(Numerator, Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(Denominator, Base)
    else:
        Numerator = int(Numerator)
        Denominator = int(Denominator)
    Common = f'{Whole}:{Numerator}|{Denominator}'
    Common = I.SimplifyRoundedCommon(Common, Base, str(RootDenominator))
    return Common


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Round Common')
        print()
        Common = input('Enter Common: ')
        Base = input('Enter Base: ')
        RootDenominator = input('Enter RootDenominator: ')
        PowerDenominator = input('Enter PowerDenominator: ')
        print()
        Common = I.RoundCommon(Common, Base, RootDenominator, PowerDenominator)
        print(Common)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break

# Python 3.9.0

# RoundRadix

def RoundRadix(Radix, Base, Place):


    '''
    Parameters:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    Place: must be a string integer that's in a base equal to the Base.

    Dependencies:
    Programmer's:
    BaseNIntegerToBaseTenInteger
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    if Base == '10':
        if len(Fraction) > int(Place):
            Fraction = f'0.{Fraction}'
            Fraction = round(float(Fraction), int(Place))
            Radix = str(float(Whole) + Fraction)
    else:
        Place = I.BaseNIntegerToBaseTenInteger(Place, Base)
        if len(Fraction) > int(Place):
            LengthOfWhole = len(Whole)
            LengthOfFraction = len(Fraction)
            LengthOfNumber = LengthOfWhole + LengthOfFraction
            Number = f'0{Whole}{Fraction}'
            Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
                      'F']
            HalfBase = round(int(Base) / 2)
            UsedDigits = Digits[:int(Base)]
            HalfOfDigits = UsedDigits[:HalfBase]
            Count = LengthOfFraction - int(Place)
            NumberList = []
            for Digit in reversed(Number):
                NumberList.append(Digit)
            CurrentDigit = NumberList[0]
            for Element in enumerate(NumberList):
                if Count == 0:
                    if CurrentDigit != Digits[int(Base)]:
                        break
                    else:
                        NumberList[Element[0]] = '0'
                        IndexOfFollowingDigit = Digits.index(NumberList[(Element[0] + 1)])
                        NumberList[(Element[0] + 1)] = Digits[(IndexOfFollowingDigit + 1)]
                        CurrentDigit = NumberList[(Element[0] + 1)]
                else:
                    if CurrentDigit in HalfOfDigits:
                        NumberList[Element[0]] = '0'
                        CurrentDigit = NumberList[(Element[0] + 1)]
                        Count -= 1
                    else:
                        NumberList[Element[0]] = '0'
                        IndexOfFollowingDigit = Digits.index(NumberList[(Element[0] + 1)])
                        NumberList[(Element[0] + 1)] = Digits[(IndexOfFollowingDigit + 1)]
                        CurrentDigit = NumberList[(Element[0] + 1)]
                        Count -= 1
            NumberList.reverse()
            if NumberList[0] == '0':
                NumberList = NumberList[1:]
            Difference = len(NumberList) - LengthOfNumber
            if Difference == 0:
                NumberList.insert(LengthOfWhole, '.')
            else:
                LengthOfWhole += Difference
                NumberList.insert(LengthOfWhole, '.')
            while NumberList[-1] == '0':
                NumberList = NumberList[:-1]
            Number = ''
            for Element in NumberList:
                Number = f'{Number}{Element}'
            if Number[-1] == '.':
                Radix = str(float(Number))
            else:
                Radix = Number
    return Radix


if __name__ == '__main__':
    import builtins
    from Module import I
    builtins.I = I
    while True:
        print()
        print('Round Radix')
        print()
        Radix = input('Enter Radix: ')
        Base = input('Enter Base: ')
        Place = input('Enter Place: ')
        print()
        Radix = I.RoundRadix(Radix, Base, Place)
        print(Radix)
        print()
        Answer = input('Would you like to keep using this program? ')
        if 'No' in Answer or 'no' in Answer or 'N' in Answer or 'n' in Answer:
            break
