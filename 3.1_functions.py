def yell(text):
    return text.upper() + '!'


# 関数はオブジェクトなので、変数に代入できる
bark = yell


def whisper(text):
    return text.lower() + '...'


# 他の関数を引数として受け取ることができる関数は「高階関数」とも呼ばれる
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


greet(bark)

greet(whisper)


# mappingするとまとめてフォーマットできる
for i in list(map(bark, ['hello', 'hey', 'hi'])):
    print(i)


# 関数は入れ子にできる
def speak(text):
    def murmur(t):
        return t.lower() + '...'
    return murmur(text)


print(speak('Hello, world'))

# speakの外でmurmurは存在しない
# print(murmur('Yo'))
# speak.murmur


# volume引数に基づいて適切な内側の関数を選択して返す
def get_speak_func(volume):
    def murmur(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return murmur
    

# 関数オブジェクトが返ってくる
print(get_speak_func(0.3))
print(get_speak_func(0.7))


# 返ってくる関数オブジェクトを変数に代入して呼び出す
speak_func = get_speak_func(0.7)
print(speak_func('Hello'))


# 内側の関数は、外側の関数の引数にアクセスできる（レキシカルクロージャ、クロージャ）
def get_speak_func2(text,volume):
    def murmur():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return murmur
    
print(get_speak_func2('Hello, world', 0.7)())


# 内側の関数を返しているfunction
# 内側の関数はレキシカルスコープから離れても外側の関数に渡された引数を記憶できる
def make_adder(n):
    def add(x):
        return x + n
    return add


plus3 = make_adder(3)
print(plus3(4))

plus5 = make_adder(5)
print(plus5(4))


# pythonでは全ての関数がオブジェクト
# オブジェクトは関数ではないが呼び出し可能にして関数のように扱うことができる
# オブジェクトのインスタンス関数として呼び出すと__call__メソッドの実行が試みられる
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x
    

plus7 = Adder(7)
print(plus7(4))


# callableはオブジェクトが呼び出し可能かをチェックする組み込み関数
print(callable(plus3))
print(callable(bark))
print(callable('hello'))

