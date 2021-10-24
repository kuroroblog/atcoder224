N = int(input())

position = []
for _ in range(N):
    x, y = map(int, input().split())
    position.append((x, y))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1, y1 = position[i]
            x2, y2 = position[j]
            x3, y3 = position[k]

            # 1点は不要になるので、座標の平行移動に利用する。
            x1 -= x3
            y1 -= y3
            # 1点は不要になるので、座標の平行移動に利用する。
            x2 -= x3
            y2 -= y3

            # 3点を繋ぎ合わせると直線になる ⏩ 原点からの傾きが等しいことを利用する。
            # 傾き : (y - 0) = a(x - 0) → a = y / x
            # (y1 - 0) / (x1 - 0) = (y2 - 0) / (x2 - 0) → y1 = (x1 * y2) / x2 → x2 * y1 = x1 * y2 → (x2 * y1) - (x1 * y2) = 0
            if (x2 * y1) - (x1 * y2) != 0:
                ans += 1

print(ans)
