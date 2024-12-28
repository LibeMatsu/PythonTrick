from string import Template


errno = 50159747054
name = 'Bob'

t = Template('Hey, $name!')

print(t.substitute(name=name))



temple_string = "Hey $name, there is a $error error!"

print(Template(temple_string).substitute(name=name, error=hex(errno)))
