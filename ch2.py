#1.자료형 변환
print('#################### 1.자료형 변환 ###################')
my_int = 1
print(type(my_int))
print(my_int)

print(type(float(my_int))) #정수형 -> 실수형 변환
print(float(my_int))

print(type(str(my_int)))  #정수형 -> 문자형 형변환
print(str(my_int))

my_str='coding'    #문자형 -> 리스트 형변환
my_list = list(my_str)
print(my_list)

#2.문자열 포맷팅
print('#################### 2.문자열 포맷팅 ###################')
my_str1 = 'My name is %s' % 'BEN'
print(my_str1)
print('%d %d' % (1,2))
print('%f' % 3.14)

my_str2 = 'My name is {}'.format('ANOLD')
print(my_str2)

print('{} X {} = {}'.format(2,3,2*3))     #format함수 활용
print('{1} X {0} = {2}'.format(2,3,2*3))  #format함수 활용시 변수 적용 순서 변경

#3.인덱싱
print('#################### 3.인덱싱 ###################')
my_name = 'Hello World!!'
print(my_name)
print(my_name[0])
print(my_name[1])
print(my_name[2])
print(my_name[-1])
print(my_name[-3])

#4.슬라이싱(Slicing)
print('#################### 4.슬라이싱(Slicing) ###################')
my_string = 'Hello World!!'
print(my_string[0:4])
print(my_string[:3])
print(my_string[2:])
print(my_string.split())  #split() 함수 사용하여 자르기 -> 공백을 기준으로 잘라서 리스트로 리턴

my_string2 = 'Hello:World!!'
print(my_string2.split(':'))  #split() 함수 사용하여 자르기 -> 특정 문자,기호 기준으로 잘라서 리스트로 리턴


#5.print-end
print('#################### 5.print-end ###################')
print('Hello world!', end='/')
print('Hello world!', end='\n')
print('Hello world!', end='\t')
print('Hello world!', end='\t')

#6.리스트2
print('\n#################### 6.리스트2 ###################')
my_list = ['테스트1','테스트2','테스트3']
print(my_list)
print(type(my_list))
my_list.append('테스트4')
print(my_list)