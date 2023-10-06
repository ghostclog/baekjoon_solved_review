#푼 날짜: 2022년 5월 9일
#난이도: 새싹
#문제 내용
'''
두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오. / 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
'''
flag = False
while(flag == False):
  a , b = map(int, input().split())
  if(a > 0 and 10 >b):
    flag = True
print(a/b)
