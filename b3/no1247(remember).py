#푼 날짜: 2023년 10월 6일
#난이도: 브3
#문제 내용
'''
N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.

총 3개의 테스트 셋이 주어진다. 각 테스트 셋의 첫째 줄에는 N(1 ≤ N ≤ 100,000)이 주어지고, 둘째 줄부터 N개의 줄에 걸쳐 각 정수가 주어진다. 주어지는 정수의 절댓값은 9223372036854775807보다 작거나 같다.
'''

import sys

rs = []
for i in range(3):
    case = int(sys.stdin.readline())
    mini_rs = 0
    for i in range(case):
        mini_rs += int(sys.stdin.readline())
    if (mini_rs > 0):
        rs.append("+")
    elif (mini_rs < 0):
        rs.append("-")
    else:
        rs.append("0")
for i in range(3):
    print(rs[i])

'''
이 레포지토리를 만들게 된 이유.
!!! input보다 readline이 반복문 내에서 더 빠르다는 사실을 깨닫게 만들어준 문제. !!!
'''
