#1.함수
print('#################### 1.함수 ###################')

def add(num1,num2):
    return num1 + num2
print(add(1,2))

def add_mul(num1,num2):     #다중 리턴값을 튜플형태로 반환
    return num1 + num2 , num1*num2
print(add_mul(1,2))

my_add , my_mul  = add_mul(1,2)  #튜플 언패킹
print(my_add)
print(my_mul)

#2.모둘
print('#################### 2.모둘 ###################')
# from 패키지명 import 모듈명  -> 이와 같은 형시으로 선언하고 함수를 활용한다.
import ch6_

ch6_.animal1()
ch6_.animal2()


