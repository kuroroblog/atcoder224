# 標準入力を受け付ける。
H, W = map(int, input().split())

A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

# 条件を満たすか確認するためのフラグを用意する。
flag = False
# 愚直にA0, 0 + A1, 1 > A1, 0 + A0, 1の場合、A0, 1 + A1, 2 > A1, 1 + A0, 2の場合...と計算する。
for i in range(H):
    for j in range(W):
        # j + 1 >= W or i + 1 >= Hを満たす時、存在しない配列を参照することになるので、その場合は検証しないことにする。
        if j + 1 >= W or i + 1 >= H:
            continue

        # Ai1, j1 + Ai2, j2 > Ai2, j1 + Ai1, j2の条件を満たす場合が見つかった時、フラグの値を変更してbreakする。
        if A[i][j] + A[i + 1][j + 1] > A[i + 1][j] + A[i][j + 1]:
            flag = True
            break

# フラグの条件によってYes, Noを出し分ける。
if flag:
    print('No')
else:
    print('Yes')
