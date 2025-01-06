'''
引数を取る関数のデコレーター
'''

def proxy(func):
    # * ←位置パラメーター, ** ←キーワードパラメーターに対する引数をすべて取得する
    def wrapper(*args, **kwargs):
        # 引数アンパック
        return func(*args, **kwargs)
    return wrapper


# 引数を取る関数のデコレーター2
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}()'
              f'returned {original_result}')
        
        return original_result
    return wrapper


@trace
def say(name, line, **kwargs):
    greeting = kwargs.get('greeting', '') + '!'
    return f'{greeting} {name}: {line}'


say('Jane', 'Hello, World', greeting='Hi')


