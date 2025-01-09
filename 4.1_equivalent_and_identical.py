'''
"is" と "=="
'''

a = [1, 2, 3]
b = a

print('a : {}'.format(a))
print('b : {}'.format(b))
# 中身が同じかどうか
print('a == b ← {}'.format(a == b))
# 指しているオブジェクトが等しいかどうか
print('a is b ← {}'.format(a is b))
print('')

# list関数を呼び出してコピーを作成
c = list(a)

print('c : {}'.format(c))
print('a == c ← {}'.format(a == c))
print('a is c ← {}'.format(a is c))
