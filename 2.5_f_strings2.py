errno = 50159747054
name = 'Bob'

print(f'Hello, {name}!')


a = 5
b = 10

print(f'Five plus ten is {a + b} and not {2* (a + b)}.')



def greet(name, question):
    return f"Hello, {name} How's it {question}?"

print(greet('Maria', 'going'))



import dis
dis.dis(greet)
