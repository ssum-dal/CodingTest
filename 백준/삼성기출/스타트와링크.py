import itertools
import sys

input = sys.stdin.readline

n = int(input())
people = [i for i in range(n)]
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

combi = list(itertools.combinations(people, int(n/2)))

answer = int(1e9)
for i in range(len(combi)//2):
    a = 0
    b = 0
    
    for x in combi[i]:
        for y in combi[i]:
            a += arr[x][y]
    
    for x in combi[-1-i]:
        for y in combi[-1-i]:
            b += arr[x][y]

    answer = min(answer, abs(a-b))

print(answer)
    