# 標準入力を受け付ける。
S = input()

lenS = len(S)

# 文字列の末尾2文字を抽出する。
# 抽出した文字列が`er`ならば`er`を返す。そうでなければ、`ist`を返す。
# 「文字列の末尾2文字を抽出する」参考 : https://www.javadrive.jp/python/string/index11.html
if S[lenS-2:lenS] == 'er':
    print('er')
else:
    print('ist')
