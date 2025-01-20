'''
全てのクラスに__repr__が必要
'''

# __repr__なし
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


my_car = Car('red', 37281)
print(my_car)
# print(my_car.color, my_car.mileage)



# __str__, __repr__を追加
# ※インタープリタセッションではオブジェクトが返る
# ※インタープリタセッションでも__repr__は働く
# ※listなどのコンテナでは__repr__が働く
class Car2:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'__str__ a {self.color} car'

    def __repr__(self):
        return f'__repr__ a {self.color} car'


my_car2 = Car2('blue', 1234)
print(my_car2)
print(str(my_car2))
print(str([my_car2]))
print(repr(my_car2))
print('{}'.format(my_car2))



# 標準ライブラリで__str__と__repr__を見てみる
import datetime

today = datetime.date.today()

print('str : {}'.format(str(today)))

print('repr : {}'.format(repr(today)))



# 完全な実装
class Car3:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r})')

    def __str__(self):
        return f'a {self.color} car'


my_car3 = Car3('white', 5555)
print(my_car3)
print(str(my_car3))
print(repr(my_car3))
