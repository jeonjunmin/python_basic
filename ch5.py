#1.if문
print('#################### 1.if문 ###################')

input_str = 'Hello'
# input_str = 'Goodbye'
# input_str = 'Good'

if (input_str == 'Hello'):
    print('{} world'.format(input_str))
elif (input_str == 'Hi'):
    print('{} world'.format(input_str))
elif (input_str == 'Goodbye'):
    print('{} world'.format(input_str))
else :
    print('{} world'.format(input_str))

#2.while문
print('#################### 2.while문 ###################')
count = 0

# while count < 3:
#     print('횟수:',count)
#     count += 1

count = 0
while count < 10:
    count += 1
    if count < 4:
        continue           #while처음으로 돌아간다.
    print('횟수:', count)
    if count ==8:
        break              #while문을 빠져나온다.


#3.딕셔너리2
print('#################### 3.딕셔너리2 ###################')

my_dict = {}
print(type(my_dict))

my_dict[0]= 'a'     #딕셔너리 키생성
my_dict[1]= 'b'
my_dict['가']= 1
print(my_dict)

del my_dict['가']    #딕셔너리 키삭제
print(my_dict)

for std in my_dict.values():   #딕셔너리에서 값만가져오는 함수
    print(std)

for std in my_dict.keys():   #딕셔너리에서 키만가져오는 함수
    print(std)

for std in my_dict.items():   #딕셔너리에서 키,값 모두 가져오는 함수
    print(std)
    my_tuple3=std
    print(my_tuple3)
