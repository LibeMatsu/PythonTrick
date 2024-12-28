# カスタムコンテキストマネージャーの作成

class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()



with ManagedFile('with_CustomContextManager.txt') as f:
    f.write('defined my own WITH stmt with CustomContextManager!!')




# デコレーターを使った作成
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


with managed_file('with_Decolator.txt') as f:
    f.write('defined my own WITH stmt with Decolator!!')
