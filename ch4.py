#1.2중for문(for x range)
print('#################### 1.2중for문(for x range) ###################')
for j in range(2,10):
    for i in range(1, 10):
        print('{}x{}={}'.format(j,i,j*i))

#2.Comprehension
print('#################### 2.Comprehension ###################')
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_nm1 = []
odd_nm2 = []

for num in numbers:
    if(num%2==1):
        odd_nm1.append(num)
print(odd_nm1)

odd_nm2 = [num for num in numbers if num%2==1]  #Comprehension사용법 -> for in문과 조건문을 한줄로 표현
print(odd_nm2)

#3.연산자
print('#################### 3.연산자 ###################')
print('Hello'+' '+'World'+'!'*3)
print(4<6)
print(4>6)
print('1.true and true = {}'.format(True and True))
print('2.true and false = {}'.format(True and False))
print('3.flase and false = {}'.format(False and False))
print('4.true or true = {}'.format(True or True))
print('5.true or false = {}'.format(True or False))
print('6.flase or false = {}'.format(False or False))
print('7.Not true = {}'.format(not True))
print('8.Not false = {}'.format(not False))

#4.멤버쉽 연산자
print('#################### 4.멤버쉽 연산자 ###################')
animals = ['호랑이','사자','독수리','기린','코끼리',]
print('호랑이' in animals)      #포함유무 여부확인 연산자
print('낙타' in animals)