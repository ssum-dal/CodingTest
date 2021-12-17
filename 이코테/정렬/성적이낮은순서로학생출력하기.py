'''
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오
'''

n = int(input())
arr = []

for i in range(n):
    name, grade = input().split()
    arr.append([name, int(grade)])

arr = sorted(arr, key=lambda x: x[1])

for i in arr:
    print(i[0], end=' ')