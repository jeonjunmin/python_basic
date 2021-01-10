import random
import logging

#1.print()
print('#################### print함수 ###################')
print('Hello World!')       #문자출력
print('My name is', 'Left') #문자출력
print([1,2,3])              #배열 출력
print(1,2)                  #다인자 출력
print(123)                  #숫자출력
print(1+2)                  #숫자연산 출력

#2.input()
print('#################### 2.input() ###################')
# age=input('당신의 나이는?')
# print(age)

#3.변수 타입
print('#################### 3.변수 타입 ###################')
my_int = 1 #정수수타입
my_float = 3.14 #실수타입
print(my_int)
print(my_float)
print(type(my_int))
print(type(my_float))
bool_true = True #참,거짓 타입
bool_false = False
print(bool_true)
print(bool_false)

#4.리스트
print('#################### 4.리스트 ###################')
my_list=['안녕',2,'하세요',3]
print(my_list)

for list in my_list:  #for 문으로 출력
    print(list)

print(random.choice(my_list))  #랜덤 출력 함수

my_list.append('여러분') #리스트에 항목 추가
print(my_list)
print(my_list[0])
my_list[0] = 'HI'
print(my_list)

#5.튜플
print('#################### 5.튜플 ###################')
my_tuple = ('요거트','레몬','시럽')
print(my_tuple)
#my_tuple[0] = '사과'  #튜플은 이런식으로 항목을 변경할 수 없음
# print(my_tuple)

#6.딕셔너리
print('#################### 6.딕셔너리 ###################')
my_dict = {'성별':'남', '나이':20 , '이름':'철수', 1:'테스트'}
print(my_dict)
print(my_dict['성별'])
print(my_dict['나이'])
print(my_dict['이름'])
print(my_dict[1])
my_dict['성별'] = '여'
print(my_dict)
print(my_dict['성별'])



