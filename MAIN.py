from class3 import Verification


class V2(Verification):

    def __init__(self, login, password):
        Verification.__init__(self, login, password)

    def save(self):
        with open('users') as r:
            for i in r:
                if (f'{self.login, self.password}' + '\n') == i:
                    raise ValueError('Такой есть')
        Verification.save(self)

    def show(self):
        return self.login, self.password


x = V2('Kenny2', '5555555555')
x.save()
