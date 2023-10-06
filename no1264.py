#푼 시각: 2023년 9월 21일
#난이도: 브4
#문제 내용
'''
영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장이 주어진다. 각 줄은 최대 255글자로 이루어져 있다.
입력의 끝에는 한 줄에 '#' 한 글자만이 주어진다.
'''

mo_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
while (True):
    count = 0
    data = input()
    if (data == "#"):
        break
    for i in mo_list:
        count += data.count(i)
    print(count)

'''
처음에 모음 대소문자가 들어있는 리스트를 만들고, #이 나올때까지 while True를 돌려준다.(이 당시에는 아직 readline이 input보다 빠르다는 사실을 몰랐음)
문장이 작성될때마다 반복문을 돌려 모음의 갯수를 센 다음 count의 숫자를 올려주고, while문을 빠져나온 뒤 count의 값을 출력시켜준다.
'''
