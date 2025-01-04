# decoratorは呼び出し可能オブジェクト
# 入力として呼び出し可能オブジェクトを受け取り、別の呼び出し可能オブジェクトを返す
def null_decorator(func):
    return func


def greet():
    return 'Hello!'


greet = null_decorator(greet)
print(greet())


# @構文を使って関数をデコレート
@null_decorator
def greet2():
    return 'Hello! 2'

print(greet2())


# デコレートされた関数の振る舞いを変更する
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet3():
    return 'Hello! 3'


print(greet3())


print(greet)
print(null_decorator(greet))
# 関数をデコレートするときに別の関数オブジェクトを返す
print(uppercase(greet))
