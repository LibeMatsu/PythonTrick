'''
カスタム例外クラスを定義する
'''
name = 'joe'

# 例外を返す関数
def validate(name):
    if len(name) < 10:
        raise ValueError("名前は10文字以上でなければなりません")
    
    
# validate(name)



# ValueErrorを継承したカスタム例外クラスを作る
class NameTooShortError(ValueError):
    pass

def validate2(name):
    if len(name) < 10:
        raise NameTooShortError(name)
    

# validate2(name)



# カスタム例外階層を作成する
class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
    pass


def validate3(name):
    if len(name) < 10:
        raise NameTooShortError("名前は10文字以上でなければなりません")
    elif len(name) > 20:
        raise NameTooLongError("名前は20文字以下でなければなりません")
    elif "cute" in name.lower():
        raise NameTooCuteError("名前が可愛すぎます")
    else:
        print(f'name: {name}')


def handle_validation_error(err):
    print(f"Validation error occurred: {err}")



try:
    validate3("justrightname")
except BaseValidationError as err:
    handle_validation_error(err)


try:
    validate3(name)
except BaseValidationError as err:
    handle_validation_error(err)



try:
    validate3('very cute cat')
except BaseValidationError as err:
    handle_validation_error(err)

