errno = 50159747054
name = 'Bob'

print('Hello, %s' % name)

print('%x' % errno)

print('Hey %s, there is a 0x%x error!' % (name, errno))

print('Hey %(name)s, there is a 0x%(errno)x error!' % {'name':'name', 'errno': 12345})
