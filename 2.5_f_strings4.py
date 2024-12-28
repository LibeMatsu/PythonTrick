SECRET = 'this-is-a-secret'

class Error:
    def __init__(self):
        pass



err = Error()

user_input = '{error.__init__.__globals__[SECRET]}'

print(user_input.format(error=err))



from string import Template

user_input2 = '${error.__init__.__globals__[SECRET]}'

print(Template(user_input2).substitute(error=err))
# フォーマット文字列がユーザーによって指定されるものである場合は、
# テンプレート文字列を使うとセキュリティ問題を回避できる
