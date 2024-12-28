class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled
    


# print(ManglingTest().get_mangled())

# print(ManglingTest().__mangled)




class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()
    

# print(MangledMethod().__method())

# print(MangledMethod().call_it())




_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled
    
print(MangledGlobal().test())




class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42


print(PrefixPostfixTest().__bam__)

