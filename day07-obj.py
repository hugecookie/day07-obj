10-1
class Thing():
    pass

Thing()
example = Thing
# print(Thing)
# print(example)

10-2
class Thing2():
    pass
example = Thing2
example.letters = 'abc'
# print(example.letters)


10-3
class Thing3():
    def __init__(self, letters):
        self.letters = letters
        print(f'문자열 {letters}를 생성합니다.')


# a = Thing3('xyz')
# print(a.letters)  # 추가적으로 객체를 생성하지 않고도 출력할 수 있다.

10-4
# class element():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#         print(f'원소 번호는 {number}번 기호는 {symbol}인 {name}이 확인 되었습니다. ')

# obj = element('Hydrogen', 'H', '1')


10-5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
# hydrogen = element(el_dict['name'], el_dict['symbol'], el_dict['number'])

10-6
# class Elements():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#         print(f'원소 번호는 {number}번 기호는 {symbol}인 {name}이 확인 되었습니다.')
#     def dump(self):
#         print(f'원소 이름은 {self.name}이고 기호는 {self.symbol}이며 원소 번호는 {self.number}입니다.')

# hydrogen = elements(el_dict['name'], el_dict['symbol'], el_dict['number'])
# hydrogen.dump()

10-7
# class Elements():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#         # print(f'원소 번호는 {number}번 기호는 {symbol}인 {name}이 확인 되었습니다.')
#     def __str__(self):
#         print(f'원소 이름은 {self.name}이고 기호는 {self.symbol}이며 원소 번호는 {self.number}입니다.')


# hydrogen = Elements(el_dict['name'], el_dict['symbol'], el_dict['number'])
# hydrogen.__str__()

10-8

# class Elements():
#     def __init__(self, name, symbol, number):
#         self.hidden_name = name
#         self.hidden_symbol = symbol
#         self.hidden_number = number
#         # print(f'원소 번호는 {number}번 기호는 {symbol}인 {name}이 확인 되었습니다.')
#
#     def get_name(self):
#         print('inside getter')
#         return print(self.hidden_name, self.hidden_symbol, self.hidden_number)
#
#     name = property(get_name)
#
# hydrogen = Elements(el_dict['name'], el_dict['symbol'], el_dict['number'])
# hydrogen.name


10-9

# class Bear():
#     def eats(self):
#         return 'Berries'
#
# be = Bear()
#
# class Rabbits():
#     def eats(self):
#         return 'clovers'
#
# ra = Rabbits()
#
# class Octothorpe():
#     def eats(self):
#         return 'campers'
#
# oc = Octothorpe()
#
# print(be.eats(), ra.eats(), oc.eats())


10-10
import random
class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class Smartphone:
    def does(self):
        return 'ring'

class Robot(Smartphone, Laser, Claw):
    obj1 = Smartphone()
    do1 = obj1.does()
    obj2 = Laser()
    do2 = obj2.does()
    obj3 = Claw()
    do3 = obj3.does()
    def __init__(self):
        num = random.randint(0, 2)
        if num == 1:
            self.do = self.do2
        else:
            self.do = self.do3

    def does(self):
        print(self.do1, self.do)

    # def does(self):
    #     return self.do1, self.do2

play = Robot()
play.does()


# print(play.does())
