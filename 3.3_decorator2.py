# 関数に複数のデコレーターを適用する
# ※ decoratorは下から順に適用される
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func):
    def wrappper():
        return '<em>' + func() + '</em>'
    return wrappper


@strong
@emphasis
def greet():
    return 'Hello!'


print(greet())


# @構文を使用しなかったとしたら・・・
def greet2():
    return 'Hello!'


decorated_greet = strong(emphasis(greet2))
print(decorated_greet())


# ※　decoratorを積み過ぎるとパフォーマンスに影響が出る可能性があるので注意
