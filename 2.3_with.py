'''
※ try...finallyで書かないと処理に失敗したときファイルディスクリプタをリークしてしまうことがある


f = open('hello.txt', 'w')
try:
    f.write('hello python!')
finally:
    f.close()

    
※ withを使うと簡単
'''


with open('hello.txt', 'w') as f:
    f.write('hello, python!')
