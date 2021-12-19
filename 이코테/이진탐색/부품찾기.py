'''
전자 매장에는 부품이 n개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 m개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
때를 놓치지 않고 손님이 문의한 부품 m개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자
'''
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
customer = list(map(int, input().split()))

#이진탐색
arr.sort()

for i in customer:
    if binary_search(arr, i, 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')

#계수 정렬
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

for i in customer:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

#집합
array2 = set(map(int, input().split()))

for i in customer:
    if i in array2:
        print('yes', end=' ')
    else:
        print('no', end=' ')