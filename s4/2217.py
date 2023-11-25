#푼 날짜: 2023년 11월 25일
#난이도: 실4
#문제 내용
'''
N(1 ≤ N ≤ 100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.
하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.

첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 자연수이다.
'''

import sys

case = int(input())

rope_list = []
rs_list = []

for i in range(case):
    rope_list.append(int(sys.stdin.readline()))

rope_list.sort()
for i in range(case):
    rs_list.append(rope_list[i] * (case - i))
rs_list.sort()
print(rs_list[case - 1])

'''
아래는 처음에 사용했던 코드다.

import sys

case = int(input())

rope_list = []
rope_dic = {}
rs_list = []

for i in range(case):
    rope_list.append(int(sys.stdin.readline()))
rope_set = set(rope_list)

for i in rope_set:
    rope_dic[i] = 0

for i in rope_list:
    for j in rope_set:
        if (i >= j):
            rope_dic[j] += 1

for i in rope_set:
    rs_list.append(i * rope_dic[i])
rs_list.sort()
print(rs_list[len(rs_list) - 1])

제출하면서도 '아 이거 타임아웃뜨겠네'라는 생각이 들었고, 결국 타임아웃이 뜨자 나는 2중 반복문을 제거하기 위해 머리를 제법 많이 굴렸다.

일단 딕셔너리 부분을 최적화 해야 할 거 같았는데... 막상 하려니까 감이 오질 않아서 처음으로 rope_list를 만드는 구간으로 돌아갔다. 그리고, 기존이랑 비슷하면서 조금 무식한 방법을 사용해보기로 했다.

바로 리스트(rope_list)를 정렬 시킨 다음, (길이*남은 로프 수)를 rs_list에 담고, rs_list를 정렬해버리는방법이다.

결과적으로 이중 반복문을 제거하느데 성공했고, 문제를 해결했다.
'''
