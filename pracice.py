
# # while 반복문

selected = None # Selected에 아무 값도 없다.
# while selected not in ['가위', '바위', '보']:
#     # [ ] 안에 input 에서 정한 값이 없을 때 까지. 
#     # 그렇지 않으면 계속 입력을 받아라. 다시 한 번 입력을 받아라. 
    
#     selected = input('가위, 바위, 보 중에 선택하세요. >')

# print('선택된 값은: ', selected )


# if selected not in ['가위', '바위', '보']:
#     selected = input('가위, 바위, 보 중에 선택하세요. >')
    
# print('선택된 값은: ', selected)

# # if 는 딱 한 번만 실행하고, while은 조건이 맞는 한 계속 실행된다. 

# # for vs while

patterns = ['가위', '보', '보']
# for pattern in range(len(patterns)):
#     print(patterns[pattern])


# while 문

length = len(patterns)
i = 0

while i < length:
    print(patterns[i])
    i = i + 1
    
# if 문은 조건이 맞으면 한 번만 실행하지만 while 반복문은 조건이 맞다면 계속 반복한다.
# for 반복문으로 짠 코드는 while 반복문으로도 작성할 수 있다.
    

numbers = [1,2,3]
length = len(numbers)
i = 0
while 
:
    print(numbers[i])
    i = i + 1
    
numbers = [1, 2, 3]
length = len(numbers)

i = 0
while i < length:
    #0 < 3 일때까지니까 0, 1, 2 세 번 반복 가능...
    print(numbers[i])
    i = i + 1
    
# # # # # # # # # # # # #   # # ## # # 

# while 문이나 for 문을 이용하면 반복문에서 break를 사용하면 반복문 전체를 빠져나오게 된다. 
# 그런데 반복문 전체를 빠져나오는 것이 아니라 해당 조건만 건너뛰고 싶을 때는 어떻게 하면 될까?
# 예를 들어, 1부터 10까지 출력하는데 5인 경우는 출력하지 않고 건너 뛰는 것을 말한다. 
# 이럴 때 사용할 수 있는 키워드가 바로 continue이다. 

# 다음 코드를 참고하면 while 문 내에 먼저 num 값을 증가하게 했습니다. 
# 그리고 *증가한 num값이 5와 같으면 * continue가 실행되도록 프로그래밍 되어있습니다.
# 파이썬 프로그램을 실행하다가 continue를 만나면, 그 아래의 코드를 수행하지 않고 while문의 조건을
# 판단하는 곳으로 점프하게 됩니다. 따라서 다음 코드를 실행하면 num값이 5일 때는 화면에 5가
# 출력되지 않은 채로 다시 while문의 조건식으로 이동하게 되고 그 다음 num += 1에 의해
# 값이 5에서 6으로 증가하게 됩니다.


# num = 0

    
# while num < 10:
#     num += 1
#     if num == 5:
#         continue
#     print(num)



list = [1, 2, 3, 5, 7, 2, 5, 237, 55]
for val in list:
    if val % 3 == 0:
        print(val)
        
        
# 딱 하나의 3의 배수만 찾고 싶다면?
for val in list: 
    if val % 3 == 0:
        print(val)
        break
    
    
# for i in range(10):
#     if i % 2 != 0:
#         print(i)
#         print(i)
#         print(i)
#         print(i)
        
# 깊은 블롤으로 들어가지 않기 위해..??

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    print(i)
    print(i)
    print(i)
        
for i in range(10):
    if i % 2 == 0:
        continue
        # i가 2의 배수라면... 처음으로 돌아가자..??
        # 제외하는 부분을 맨 처음으로 처리... 
    print(i)
    print(i)
    print(i)
    print(i)
    
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            # n = 2, 3, 4, 5, 6, 7, 8, 9
            # x = #  23, 234, 2345, 23456, 234567, 2345678
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
            

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
        
# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops


sizes = [33,35,34,37,32,35,39,32,35,29]
for i,size in enumerate(sizes):
    if size == 32:
        print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
        break
        # 여기에 코드를 추가하세요
        
        
        
# sizes에는 진열된 바지 사이즈의 목록이 들어 있습니다. 다음 코드 사이즈가 32인 바지의
# 위치를 출력하고 있다. 5번째 줄을 수정해서 사이즈가 32인 바지의 위치를 한 번만 


# 다음 코드는 numbers에 있는 튜플을 받아들여서 튜플을 첫번째 숫자를 두 번째 숫자로 나누는
# 역할을 합니다. 이때, b가 0이면 "0으로 나눌 수 없다" 고 출력하는데요.
# 이 if else 문에서 continue문을 사용하여 else를 사용하지 않도록 변경해 보세요. 


numbers = [ (1,2),(10,0) ]
##############################################
a, b = numbers  # 의 결과와
a, b in numbers # 의 결과가 다른 이유?


type(numbers)

a, b = numbers
a # tuple
b
a / b

for a, b in numbers:
    # tuple로 받아들인다. 
    # numbers = [(1, 2), (10, 0)]
    # a = 1, 10... b = 2, 0
    # [(a, b), (a, b)]
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
    else:
        # 이 부분이 else문에 들어있지 않도록 수정해야 합니다.
        print("{}를 {}로 나누면 {}".format(a,b,a/b))

# continue는 다른 조건은 생각하지 않고, 지정된 조건만 생각하게 한다. 

for a, b in numbers:
    print(a)
    
for a, b in numbers:
    print(a, b)
    
a, b in numbers
a



numbers = [(1, 2), (10, 0)]
for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
    else:
        # 이 부분이 else 문에 들있지 않도록 수정해야 합니다.
        print("{}를 {}로 나누면 {}".format(a, b, a/b))
        
numbers = [ (1,2),(10,0) ]

for a,b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue
    print("{}를 {}로 나누면 {}".format(a,b,a/b))
# if문의 아래에 print가 들어가면 if의 종속절이 되기 때문에, continue에서 걸러짐
        
for a, b in numbers:
    if b
    
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
