#푼 날짜: 2023년 10월 6일
#난이도: 브3
#문제 내용
'''
재석이는 대문에 붙이는 (주소를 나타내는) 호수판 제작업체의 직원이다. 고객에게 전달할 호수판은 숫자와 숫자 사이 그리고 왼쪽 오른쪽으로 적당히 여백이 들어가 줘야하고 숫자마다 차지하는 간격이 조금씩 상이하다. 다행이도 규칙은 매우 간단하다. 

각 숫자 사이에는 1cm의 여백이 들어가야한다.
1은 2cm의 너비를 차지해야한다. 0은 4cm의 너비를 차지해야한다. 나머지 숫자는 모두 3cm의 너비를 차지한다.
호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.
예를 들어 120 같은 경우,  각 숫자 사이에 여백이 1cm 씩 2개 들어간다. 1은 2cm, 2는 3cm, 0은 4cm를 차지한다. 오른쪽, 왼쪽 경계에서 각각 여백이 1cm씩 차지한다. 따라서 총 2 + 2 + 3 + 4 + 1 + 1 = 13(cm) 가 된다.
재석이는 고객에게 전달해야할 호수판의 너비가 얼마나 되는지 궁금해졌다. 재석이를 도와주자!

호수판에 들어갈 숫자 N의 범위는 1 ≤ N ≤ 9999 이다.
입력은 마지막에 0이 들어오기 전까지 계속해서 줄 단위로 주어진다.
또한, 마지막의 0은 처리하지 않는다.
'''

import sys

rs = []
while (True):
    zip_code = int(sys.stdin.readline())
    if (zip_code == 0):
        break
    zip_code = str(zip_code)
    zip_lenght = len(zip_code)
    need_lenth = 2 + int(zip_lenght) - 1

    zip_lenght -= zip_code.count('1')
    zip_lenght -= zip_code.count('0')

    need_lenth += zip_lenght * 3
    need_lenth += int(zip_code.count('1')) * 2
    need_lenth += int(zip_code.count('0')) * 4
    rs.append(need_lenth)
for i in rs:
    print(i)

'''
반복문 안에서 입력을 받아야하는 상황이 나와서 sys.stdin.readline()를 썼다만... 줄내림 문자가 같이 zip_code 변수 안으로 들어오는 바람에 해당 부분을 제거하는 과정에서 코드가 다소 지저분해졌다.
'''
