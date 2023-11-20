date = "2020-03-24"
date.split("-")

a = "2020/03/24"
a.split("/") # /를 기준으로 나눈다

name = "KAKAO"
new_name = 'T' + name[1:] #1번
new_name2 = name.replace('K','T',1) #replace('지정 단어', '바굴 단어', '몇 개')
new_name
new_name2

len(date) #len = 글자수

code = "  055093  "
code = code.split()
code

close = "63,000,000"
close.replace(",", "")

close2 = 63100000
format(close2, ",d") # 천 단위로 ,를 붙인다.

s = "Daum Kakao"
daum = s[0:4]
kakao = s[-5:]
kakao + ' ' + daum
