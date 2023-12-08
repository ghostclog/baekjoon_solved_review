'''
#푼 날짜: 2023년 12월 5일
#난이도: 실버 3
#문제 내용
조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
조규현의 좌표 (x_1, y_1)와 백승환의 좌표 (x_2, y_2)가 주어지고, 조규현이 계산한 류재명과의 거리 r_1과 백승환이 계산한 류재명과의 거리 r_2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.
한 줄에 공백으로 구분 된 여섯 정수 x_1, y_1, r_1, x_2, y_2, r_2가 주어진다.
'''
#원이 접하는, 접하지 않는 케이스 분류
"""
한 점만 접하는경우
- 두 원의 반지름의 합이 두 점의 거리와 같을때(두 반지름 = 거리)

두 점이 접하는 경우
- 두 원의 거리가 두 원의 반지름의 합보다 작을때
- 두 원의 거리와 작은 원의 반지름의 합이 큰 원의 반지름보다 작지 않을때.

원이 접하는 않는 경우
- 두 원의 반지름의 합이 두 점의 거리보다 작을때(두 반지름 < 거리)
- 두 원의 거리와 작은 원의 반지름의 합이 큰 원의 반지름보다 작을때.

입력
케이스 수
1번 터렛의 x y / 2번 터렛의 x y / 1번 터렛의 거리 / 2번 터렛의 거리
두 원의 거리 = ((x1-x2)제곱 + (y1-y2)제곱)의 제곱근(math.sqrt)
1번 터렛의 반지름  > 1번 터렛의 거리 / 2번 터렛의 반지름 > 2번 터렛의 거리
"""
import math

case = int(input())
rs_list = []

for i in range(case):
    #1번 터렛 위치/터렛의 반지름 / 2번 터렛의 위치 / 2번 터렛 반지름
    x1, y1, x_distance, x2, y2, y_distance = map(int, input().split())

    # 두 점의 거리 구하기
    terrets_distance = math.sqrt(
        math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

    #짧은 반지름. 큰 반지름 구분하기
    small_dis = y_distance
    big_dis = x_distance
    if (x_distance < y_distance):
        small_dis = x_distance
        big_dis = y_distance

    #접점 판단하기

    # 동심 원일때
    if (terrets_distance == 0 and x_distance == y_distance):
        rs_list.append(-1)

    #반지름의 합과 두 점 사이가 같은 경우 / 두 점 사이와 작은 반지름의 합이 큰 반지름과 같은 경우 >> 접점이 하나
    elif (terrets_distance == x_distance + y_distance
          or (terrets_distance + small_dis == big_dis)):
        rs_list.append(1)

    #반지름의 합이 두 점 사이보다 큰 경우. 그리고, 동시에 두 점 거리와 작은 반지름의 합이 큰 반지름보단 클 때 >> 접점이 두 개
    elif ((terrets_distance < x_distance + y_distance)
          and (terrets_distance + small_dis > big_dis)):
        rs_list.append(2)

    # 그 밖의 경우는 접점이 없음
    else:
        rs_list.append(0)

for i in rs_list:
    print(i)

'''
터렛의 좌표와 거리를 원의 좌표와 반지름이라 가정하고, 두 원이 접하는 경우에 대해 모두 구하면 쉽게 풀 수 있다.

사실 좀 많이 틀렸다.
'''
