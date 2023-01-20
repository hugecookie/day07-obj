# 10.3 Inheritance

# class Car():
#     pass
#
# class Yugo(Car):
#     pass
# print(issubclass(Yugo, Car))

# give_me_a_car = Car()
# give_me_a_yugo = Yugo()


# class Car():
#     def exclaim(self):
#         print("I'am a car!")
#
# class Yugo(Car):
#     pass
#
# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
#
# give_me_a_car.exclaim()
# give_me_a_yugo.exclaim()  # Yugo 객체에서도 exclaim 객체를 사용가능하다.

# class Car():
#     def exclaim(self):
#         print("I'am a car!")
#
# class Yugo(Car):
#     def exclaim(self):
#         print("I'am a Yugo! Much like a Car, But more Yugo-ish!")
#
# My_car = Yugo()
# My_car.exclaim()


# 10.3.4 super()

class Pokemon:
    def __init__(self, owner, skills): # 객체 초기화 메서드
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성됨 :", end=' ')
    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        # for i in range(len(self.skills)):
        #     print(f'{i+1}: {self.skills}')
        # print(f"기술의 이름은 {self.skills} 입니다.")
        for skill in self.skills:
            print(skill, end=' ')
        print('')
    def attack(self, idx):  # override
        print(f'{self.owner}의 포켓몬 {self.skills[idx]} 공격 시전!')


class Pikachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # Pokemon 초기화 메서드 __init__ 실행
        self.name ="피카츄"
        print(f'피카츄')

    def attack(self, idx):  # override
        print(f'{self.owner}의 포켓몬 {self.name}가 {self.skills[idx]} 공격 시전!')


class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # Pokemon 초기화 메서드 __init__ 실행
        self.name ="꼬부기"
        print(f'꼬부기')

    def attack(self, idx):  # override
        print(f'{self.owner}의 포켓몬 {self.name}이/가 {self.skills[idx]} 공격 시전!')

    def swim(self):  # 꼬부기만 가지고 있는 기능 실행
        print(f'{self.name}가 수영을 실행!')


class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # Pokemon 초기화 __init__ 실행
        self.name ="파이리"
        print(f'파이리')

    def attack(self, idx):  # override
        print(f'{self.owner}의 포켓몬 {self.name}이/가 {self.skills[idx]} 공격 시전!')


# while True:
#     menu = input('1) 포켓몬 생성  2) 포켓몬 정보  3) 공격  4) 프로그램 종료 :')
#     if menu == '4':
#         print('프로그램을 종료합니다.')
#         break
#     elif menu == '1':
#         pokemon = int(input('1) 피카츄  2) 꼬부기  3) 파이리'))
#         if pokemon == 1:
#             name = input('플레이어의 이름 입력 :')
#             s = input('사용 가능한 기술의 입력(/로 구분)')
#             p = Pikachu(name, s)
#         elif pokemon == 2:
#             name = input('플레이어의 이름 입력 :')
#             s = input('사용 가능한 기술의 입력(/로 구분)')
#             p = Ggoboogi(name, s)
#         elif pokemon == 3:
#             name = input('플레이어의 이름 입력 :')
#             s = input('사용 가능한 기술의 입력(/로 구분)')
#             p = Pairi(name, s)
#         else:
#             print('메뉴에서 골라 주세요.')
#         info_attack = input('1) 정보조회  2) 공격')
#         if info_attack == '1':
#             p.info
#         elif info_attack == '2':
#             p.info()
#             attack_menu = input('공격번호 선택 :')
#             p.attack(int(attack_menu)-1)
#         else:
#             print('메뉴에서 골라주세요.')
#
#
#     elif menu == '2':
#         pass
#     elif menu == '3':
#         pass
#     else:
#         print('잘못 입력 하셨습니다. 다시 시도해 주세요.')


# p0 = Pokemon('바람', '어떤공격')
# p0.attack(0)

# pi1 = Pikachu('전기', '번개/백만 볼트/아이언 테일')
# ggo1 = Ggoboogi('물', '고속 스핀/물대포/몸통 박치기')
# pai1 = Pairi('불', '화염, 깨물기, 돌진')
# ggo1.info()
# num = int(input('어떤 기술을 사용 하시겠습니까? 1)고속 스핀 2)물대포 3)몸통 박치기'))
# ggo1.attack(num-1)


# 10.3.5 Multiple Inheritance


class Animal():
    def says(self):
        return '동물!'

class Horse(Animal):
    def says(self):
        return '말!'
    # pass

class Donkey(Animal):
    def says(self):
        return '당나귀!'
    # pass

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    # def says(self):
    #     return '하니!'
    pass

m1 = Mule()
h1 = Hinny()
# print(h1.says())
# print(m1.says())
#
# print(m1.says())

# 10.3.6 mixins


class PrettyMixin:
    def time_print(self):
        import datetime
        print(datetime.date.today())

    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


# t = Thing()
# t.time_print()
# t.name = "Nyarlathotep"
# t.feature = "ichor"
# t.age = "eldritch"
# t.gender = "female"
# t.gender = "male"
# t.dump()


# 10.5.2 Getter/Setter method

class Duck:
    color = 'White'
    def __init__(self, input_name):
        self.__hidden_name = input_name

    @staticmethod
    def test():
        print('정적 메서드')

    @classmethod
    def ace(cls):
        print('클래스 메서드')


    @property
    def name(self):
        print('inside the getter')
        return self.__hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__hidden_name = input_name
    # name = property(get_name, set_name)


# don = Duck('Donald')
# print(don.name, Duck.test(), don.ace(), don.test())
# print(don.color, Duck.color)
# don.color = 'blue'
# print(don.color, Duck.color)
# Duck.color = 'green'  # 클래스 변수 값 변경
# print(don.color, Duck.color)
# d2 = Duck('Induk')
# print(don.color, Duck.color, d2.color)

# # print(don.get_name())
# print(don.name)
# don.name = 'Donna'
# # print(don.set_name('Donna'))
# print(don.name)
# don.__hidden_name = 'Hwa Rang'
# print(don.name)
# don.name = 'Hwa Rang'
# print(don.name)

# 10.5.4 Properties for Computed Values

class circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self, radius):
        return 2 * radius



# 10.5.6 클래스와 개체 속성

class fruit():
    color = 'red'

blueberry = fruit


# 10.6.2 Class method

class A:
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod  # @classmoethod를 가지고 있는 객체들만 공유한다.
    def kids(cls):
        print("A has", cls.count, "little objeccts.")


# easy_a = A()
# breezy_a = A()
# wheezy_a = A()
# A.kids()


# 10.6.3 Static Method


class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

# CoyoteWeapon.commercial()


# 10.7 Duck Typing

# class Quote():
#     def __init__(self, person, words):
#         self.person = person
#         self.words = words
#     def who(self):
#         return self.person
#     def says(self):
#         return self.words + '.'

import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Thing(PrettyMixin):
    pass
    def get_area(self):
        print('도형의 면적을 출력합니다')

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

    def __del__(self, other):
        return  math.pi * self.radius * self.radius -math.pi * other.radius * other.radius


class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y, radius)
        self.height = height

    def get_area(self):  # get_volume
        return super().get_area() * self.height


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def __add__(self, other):
        # 두 사각형 넓이의 합
        return (self.width * self.length) + (other.width * other.length)
        # 각 사각형 width의 합과 length의 합의 곱
        # return Rectangle(0, 0, (self.width+other.width), (self.length+other.length))


cy1 = Cylinder(20, 20, 10.0, 2)
c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 50, 5, 2)
r2 = Rectangle(70, 30, 10, 15)
print(cy1.get_area())
print(f'사각형의 좌표는 x:{r1.x}, y:{r1.y}이고 넓이는 {r1.get_area()}입니다')
print(c1.get_area())
print(c2.get_area())
print(r1 + r2)
# c1 = Circle(100, 100, 10)
# c2 = Circle(50, 50, 2)
# r1 = Rectangle(100, 50, 5, 2)
# print(f'사각형의 좌표는 x:{r1.x}, y:{r1.y}이고 넓이는 ')
# print(c1.get_Area())
# print(c2.get_Area())



class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

a = Word('acE')
b = Word('Ace')
# cy1 = Cylinder(20, 20, 10, 5)
# r1 = Rectangle(20, 20, 10, 5)
# r2 = Rectangle(20, 20, 10, 5)

# print(r1+r2)
# print(a.__eq__(b))
# print(a == b)
