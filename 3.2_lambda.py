add_lambda = lambda x, y: x + y

print(add_lambda(5, 3))


def add(x, y):
    return x + y

print(add(5, 3))


# lamdaで関数式を一行で定義、すぐに呼び出す
(lambda x, y: print(x + y))(5, 3)


# lambdaには暗黙のreturnが常に存在する
print((lambda x, y: x + y)(5, 3))


# lambdaはこういう時便利
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(tuples)
print(sorted_tuples)


# こういう時便利
num = sorted(range(-5, 6), key=lambda x: x * x)
print(num)


# lambdaもレキシカルクロージャとして機能する
def make_adder(n):
    return lambda x : x + n

plus3 = make_adder(3)
print(plus3(4))

plus5 = make_adder(5)
print(plus5(4))



# ※ lambdaは便利な時もあるけれど、可読性が低くなることがある
# ※ lambda関数は控えめに、十二分の注意を払って使用すべきである


# NG
print(list(filter(lambda x: x % 2 == 0, range(16))))

# こちらのほうが望ましい
print([x for x in range(16) if x % 2 == 0])
