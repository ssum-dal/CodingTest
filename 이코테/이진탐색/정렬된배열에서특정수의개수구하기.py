'''
n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
이때 이 수열에서 x가 등장하는 횟수를 계산하라
예를 들어 수열 [1,1,2,2,2,2,3]이 있을 때 x=2라면, 현재 수열에서 값이 2인
원소가 4개이므로 4를 출력한다. (없으면 -1)
'''

def find_first(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
    
        if (arr[mid] == target) and (mid == 0 or arr[mid-1] < target):
            return mid
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return -1

def find_last(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if (arr[mid] == target) and (mid == n-1 or arr[mid+1] > target):
            return mid
        elif arr[mid] <= target:
            start = mid + 1
        else:
            end = mid -1
    return -1

n, target = map(int, input().split())
arr = list(map(int, input().split()))

first = 0
last = 0

first = find_first(arr, target, 0, n-1)

if first == -1:
    print(-1)
else:
    last = find_last(arr, target, 0, n-1)
    print(last-first+1)