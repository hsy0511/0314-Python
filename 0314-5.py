# quiz
'''
조건1: 댓글 20명 아이디 20개
조건2: 무작위로 추첨 중복 x
조건3: random 모듈 shuffle , sample 활용
'''

from random import * # random 모듈 import
a = range(1,21) # 1~20까지 범위 설정
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # 1~20까지 리스트 작성
print(type(a)) # a 자료형 형태 파악
print(type(b)) # b 자료형 형태 파악
print(list(a)) # a 자료형 리스트로 변환
shuffle(b) # b 리스트 값 혼합하여 섞기
print(b)
print('---당첨자 발표---')
c = sample(b,1) # b 자료형에서 1개 랜덤으로 뽑고 리스트로 변환
print('치킨 당첨자 : ',end='') # ,end=''를 통해 한줄로 붙여쓰기 (\n과 같음) 
print(c[0]) # c의 0번째 인덱스 값 인덱싱
print('커피 당첨자 : ',end='')
print(sample(a,3)) # a 자료형에서 3개 랜덤으로 뽑고 리스트로 변환
print('----축하합니다----')