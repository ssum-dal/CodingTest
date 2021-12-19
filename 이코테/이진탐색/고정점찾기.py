'''
기출 28
고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.
예를 들어 수열 a={-15, -4, 2, 8, 13}이 있을 때 a[2] = 2 이므로, 고정점은 2가 된다.
하나의 수열이 n개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있다.
이때 수열에서 고정점이 있다면 고정점을 출력하는 프로그램을 작성하라(고정점은 최대 1개, 없다면 -1)
'''

def binary_search(arr, start, end):
    while start <= end:
        mid = (start+end)//2

        if mid == arr[mid]:
            return arr[mid]
        elif mid < arr[mid]:
            end = mid -1
        else:
            start = mid + 1
    return -1


n = int(input())
arr = list(map(int, input().split()))

print(binary_search(arr, 0, n-1))
