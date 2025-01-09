'''
引数のアンパック
'''

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

print_vector(0, 1, 0)


# タプルやリストのデータがあるとする
tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]

# 普通にタプルを渡すならこんな（めんどくさい）
print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])

# *演算子による引数のアンパックを使ってみる（すごい）
print_vector(*tuple_vec)
print_vector(*list_vec)
print('')

genexpr = (x * x for x in range(3))
print(genexpr)
print_vector(*genexpr)
print('')

# ディクショナリのアンパックには**演算子を
# ディクショナリには準者がないので、値はキーに基づいて照合される
dist_vec = {'y': 0, 'z': 1, 'x': 1}
print(dist_vec)
print_vector(**dist_vec)
print('')

print_vector(*dist_vec)
print('')
