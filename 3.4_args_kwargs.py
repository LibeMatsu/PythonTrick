
'''
*args と **kwargs
'''

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


# required(必須)パラメーターを指定しないとエラーになる
# print(foo())

print(foo('hello'))
print('')

print(foo('hello', 1, 2, 3))
print('')

print(foo('hello', 1, 2, 3, key1='value', key2=999))
print('')


# スーパークラスの振る舞いを拡張
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'


print(AlwaysBlueCar('green', 48392).color)
