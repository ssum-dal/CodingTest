'''
수열을 내림차순으로 정렬하는 프로그램을 만드시오
'''

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    print(i, end=' ')