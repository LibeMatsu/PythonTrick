errno = 50159747054
name = 'Bob'

print('Hello, %s' % name)

print('%x' % errno)

print('Hey %s, there is a 0x%x error!' % (name, errno))

print('Hey %(name)s, there is a 0x%(errno)x error!' % {'name':'name', 'errno': 12345})



errno = 123456789
name = 'Micky'

print('Hello, {}'.format(name))

print('Hey {name}, there is a ox{errno:x} error!' .format(name=name, errno=errno))

