'''
재귀를 이용한 풀이 top down 방식
큰 문제를 해결하기 위해 작은 문제를 호출
'''
d = [0]*100

def fibo(x):
    print('f('+str(x)+')', end=' ')
    if x==1 or x==2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1)+fibo(x-2)
    
    return d[x]

#print(fibo(5))

'''
반복문을 이용하는 풀이 bottom up
다이내믹 프로그래밍의 전형적인 형태
'''

d[1] = 1
d[2] = 1

n = 99

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])