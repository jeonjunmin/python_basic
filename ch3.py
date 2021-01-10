#1.인덱싱2
print('#################### 1.인덱싱2 ###################')
animals = ['코알라','사자','호랑이','팬더','하마']
print(animals)
animals.append('코알라')  #리스트 항목 추가
print(animals)
del animals[5]    #리스트 항목 지우기
print(animals)

#2.리스트 메소드
print('#################### 2.리스트 메소드 ###################')
animals.append('f')
animals.append('a')
animals.append('사자')
animals.sort()     #가,나,다 / abc 순 정렬
print(animals)
print(len(animals))   #len메소드 -> 항목갯수
print(animals.count('사자'))  #count메소드 -> 리스트안에 해당 항목이 몇개 들어있는지 카운트

#3.튜플
print('#################### 3.튜플 ###################')
my_tuple = ()
print(type(my_tuple))
my_tuple = (1,2,3)
print(my_tuple)

#4.Packing , Unpacking
print('#################### 4.Packing , Unpacking ###################')
my_tuple1 = 1,2,3
print(type(my_tuple1))
print(my_tuple1)
num1 , num2 , num3 = my_tuple1
print('num1---> {} '.format(num1))
print('num2---> {} '.format(num2))
num1 , num2  = num2 , num1      #튜플의 패킹, 언패킹
print('num1---> {} '.format(num1))
print('num2---> {} '.format(num2))


#5.for문
print('#################### 5.for문 ###################')
for animal in animals:
    print(animal)

for str in 'Hello World!!!':
    print(str)


#6.range
print('#################### 6.range ###################')
print(range(3))
print(type(range(3)))

for n in [0,1,2]:
    print(n)

for n in range(0,3):  #0부터 3개원소 출력 -> [0,1,2]랑 같음
    print(n)

for n in range(3,100):  #=[3,4,5, .... ,97,98,99]  ex)range(n,k) => [n, ... , k-1]  n부터 k-1까지
    print(n)

