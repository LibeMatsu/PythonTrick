'''
趣味と実益を兼ねたクローンオブジェクトの作成
'''

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 浅いコピーを作成
ys = list(xs)

print(xs)
print(ys)
print('')

xs.append(['new sublist'])
print(xs)
print(ys)
print('')


xs[1][0] = 'X'
print(xs)
print(ys)
print('')

