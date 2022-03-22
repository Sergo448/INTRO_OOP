from class3 import Verification
from tkinter import Tk, Button
from A_B_C_D import A, B, C, D


class V2(Verification):

    # Простое наследование
    def __init__(self, login, password, age):
        # Verification.__init__(self, login, password)
        super().__init__(login, password)
        self.__save()
        self.age = age

    def __save(self):
        with open('users') as r:
            for i in r:
                if (f'{self.login, self.password}' + '\n') == i:
                    raise ValueError('Такой есть')
        # Verification.save(self)
        super().save()

    def show(self):
        return self.login, self.password


"""class My_app(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x400')
        self.setUI()

    def setUI(self):
        Button(self, text='OK').pack()"""

x = V2('Bob', '000000000', 33)
