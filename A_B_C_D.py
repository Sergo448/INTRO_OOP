class A:
    def a(self):
        print('A')


class B:
    def a(self):
        print('B')


class C(B):
    def a(self):
        print('C')


class D(C, A):
    def a(self):

        super(D, self).a() # От класса D начинаем происк метода а()
        # super(D).a()
        # Поиск в глубину
        # print(self.__class__.__mro__)


# print(D.__mro__)
D().a()