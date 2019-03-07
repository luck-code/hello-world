import one
import two



def main():
    first = one.One()
    first.sum(2, 3)
    print(first.sum(first.a, first.b))

#

    second = two.Two()
    perem = first.sum(10, 10)
    print("down mul func")
    two.Two.a = 14
    two.Two.b = 00
    second.mul()


#   Задание аргументов класса вне его тела
    two.Two.buf = 100
    hey = two.Two.buf
    print(hey)


if __name__ == '__main__':
    main()
