class Indenter:
    # 初期化
    def __init__(self):
        self.level = 0

    # with文に入る時
    def __enter__(self):
        self.level += 1
        return self
    
    # with文を抜ける時
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)



print('first')


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
