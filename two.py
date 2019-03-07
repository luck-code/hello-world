# Вложенность классов
class TestBaseClass:
    a = 1
    b = 2

    class TestClassIntoClass:
        aa = 11
        bb = 22


class TestBaseClass2:
    c = 3
    d = 4


# Наследование
class Nasledovanie(TestBaseClass, TestBaseClass2):
    pass


# print("Доступ во вложенный класс: " + str(Nasledovanie.TestClassIntoClass.aa))
# print("Наследование:" + str(Nasledovanie.a) + str(Nasledovanie.d))

# Неявные атрибуты
# print(Nasledovanie.__name__ + ' - базовые классы: ' + str(Nasledovanie.__bases__))
# print(Nasledovanie.__name__, Nasledovanie.__bases__)


class Two:
    """
    Description of a class with special implicit attribute __doc__ in class
    """
    a = 5
    b = 10

    __doubleunderscope = 666
    _underscope = 777
    __outinit = "__outinit"

    multiply = __doubleunderscope * _underscope

    def mul(self):
        c = self.a * Two.b
        c = self.__doubleunderscope + Two._underscope
        print("Сумма _ и __ атрибутов: ", str(c))

    def __init__(self):
        self.__var = "Старое значение частного атрибута"
        self.__ininit = "__ininit"

    def print_var(self):
        print(self.__var)


x = Two()
print("Список атрибутов и их значений: ", x.__dict__)
print("НИЖЕ печать частного атрибута __var ДО его изменения: ")
x.print_var()
x._Two__var = "Новое значение"
print("Печать частного атрибута __var ПОСЛЕ его изменения: ", x._Two__var)
print("__пер внутри __инит__: ", x._Two__ininit)
print("__пер вне __инит__: ", x._Two__outinit)
# print("test:", str(Two.print_var(x)))


class Three:
    pass
Three.x = 23
# print(Three.x)  # Переменная заданная вне тела класса
# print(Three.__name__) # Вывод неявного атрибута

print("Произведение частных переменных: ", str(Two.multiply))
print(Two.__doc__)

obj = Two()
obj.mul()

print("Вывод _ атрибута: ", obj._underscope)
print("Вывод __ атрибута через _Two__attrname: ", obj._Two__doubleunderscope)
# print(obj.__doubleunderscope) - не работает

# Дескрипторы
class Desc:
    def __init__(self, value):
        self.desc = "Начальное значение"

    def __set__(self, *_):
        pass  # При pass игнорируются попытки установки нового значения
        # self.desc = "Насильно перезапись"  # При попытке установить новое
                                           # значение всегда перезаписывается
                                           # на это

    def __get__(self, *_):
        return self.desc


class X:
    c = Desc(12)


x = X()
x.c = 77

print("Дескриптор desc: ", x.c)

print("obj.a: " + str(obj.a))
# print(obj.a.__getattribute__(str(obj.a)))

class Test:
    a = 1


t = Test()
print(t.a.__getattribute__(str(t.a)))


