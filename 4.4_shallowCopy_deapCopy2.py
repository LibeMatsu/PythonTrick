'''
趣味と実益を兼ねたクローンオブジェクトの作成
'''

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 深いコピーを作成
import copy

zs = copy.deepcopy(xs)

print(xs)
print(zs)
print('')

xs.append(['new sublist'])
print(xs)
print(zs)
print('')


xs[1][0] = 'X'
print(xs)
print(zs)
print('')
