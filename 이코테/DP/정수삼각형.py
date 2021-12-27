'''
https://www.acmicpc.net/problem/1932
'''

n = int(input())
d = []

for i in range(n):
    d.append(list(map(int, input().split())))

for x in range(1, n):
    for y in range(0, x+1):

        if y == 0:
            left = 0
        else:
            left = d[x-1][y-1]
        
        if y == x:
            right = 0
        else:
            right = d[x-1][y]
      
        d[x][y] = d[x][y] + max(left, right)

print(max(d[n-1]))
