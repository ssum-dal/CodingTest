'''
다시 풀어보기
'''

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split( )))
    d = []
    
    for i in range(0, n*m, m):
        d.append(tmp[i : i+m])

    for y in range(1, m):
        for x in range(n):
            if x == 0:
                left_up = 0
            else:
                left_up = d[x-1][y-1]

            if x == n-1:
                left_down = 0
            else:
                left_down = d[x+1][y-1]

            left = d[x][y-1]
            d[x][y] = d[x][y] + max(left_up, left, left_down)

    answer = 0
    for i in range(n):
        answer = max(answer, d[i][m-1])

    print(answer)

            
            
