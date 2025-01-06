'''
デバッグ可能なデコレーターを書く
'''

# 元の関数の名前、docstring、パラメーターはラッパークロージャに隠されてしまう
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


def greet():
    """Return a friendly greeting."""
    return 'Hello!'


decorated_greet = uppercase(greet)


print(decorated_greet())

print(greet.__name__)
print(greet.__doc__)
# ↓ ラッパークロージャを適用したケース ↓
print(decorated_greet.__name__)
print(decorated_greet.__doc__)


# functools.wrapsを使用する
import functools

def uppercase2(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


@uppercase2
def greet2():
    """Return a friendly greeting2."""
    return 'Hello!'


# 入力関数のdocstringやその他のメタデータが引き継がれる
print(greet2.__name__)
print(greet2.__doc__)
