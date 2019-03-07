class Variable:
    def __init__(self):
        self.__var = 123

    def print_var(self):
        print(self.__var)


x = Variable()
x.print_var()

x._Variable__var = 456
x.print_var()
