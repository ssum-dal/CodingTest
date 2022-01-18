#https://www.acmicpc.net/problem/14891

# n극 0 s극 1
# 시계 1 반시계 -1

def rotate(index, rot):
    global st
    st[index] = st[index][rot*-1:] + st[index][:rot*-1]

def left(index, rot):
    if index == -1 or st[index][2] == st[index+1][6]:
        return
    left(index-1, rot*-1)
    rotate(index, rot)

def right(index, rot):
    if index == 4 or st[index][6] == st[index-1][2]:
        return
    right(index+1, rot*-1)
    rotate(index, rot)

st = []
for _ in range(4):
    st.append(list(map(int, input())))

t = int(input())

for _ in range(t):
    index, rot = map(int, input().split())

    if index > 1 and st[index-1][6] != st[index-2][2]:
        left(index-2, rot*-1)
    if index < 4 and st[index-1][2] != st[index][6]:
        right(index, rot*-1)
    
    rotate(index-1, rot)

answer = 0
for i in range(4):
    if st[i][0] == 1:
        answer += 2**i
print(answer)
    

    