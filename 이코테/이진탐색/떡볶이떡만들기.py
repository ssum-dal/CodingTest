'''
떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는
15, 14, 10, 15cm가 될 것이다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다.
손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 m일 때 적어도 m만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
'''

def binary_search(dduck, target, start, end):
    global answer
    
    while start <= end:
        mid = (start+end)//2
        rest = 0
        for i in dduck:
           if i > mid:
               rest += i - mid

        if rest < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1 

answer = 0
n, m = map(int, input().split())
dduck = list(map(int, input().split()))

dduck.sort()
end = max(dduck)

binary_search(dduck, m, 0, end)

print(answer)
