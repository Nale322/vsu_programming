class Time:

    def __init__(self):
        self.hours = None
        self.minutes = None
        self.seconds = None

    def inputthis(self):
        self.hours = input('Input hour please: ')
        self.minutes = input('Input minutes please: ')
        self.seconds = input('Input seconds please: ')

    def writeln(self):
        print('The time is: ', self.hours, ':', self.minutes, ':', self.seconds)

a = Time()
a.inputthis()
a.writeln()