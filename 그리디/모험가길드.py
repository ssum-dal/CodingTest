'''
한 마을에 모험가 N명이 있다. 모험가 길드에서는 N명의 모험가를 대상으로 공포도를 측정했는데
공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다.
길드장은 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한
모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했다.
최대 몇 개의 모험가 그룹을 만들 수 있는가(모든 모험가를 특정한 그룹에 넣을 필요는 없다)
'''

n = int(input())
adventurer = list(map(int, input().split()))
result = 0

adventurer.sort()

member = 0
for i in adventurer:
    member += 1
    if(i <= member):
        result += 1
        member = 0

print(result)
