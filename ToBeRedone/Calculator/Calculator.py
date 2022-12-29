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
