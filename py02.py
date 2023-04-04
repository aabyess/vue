
str = "파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은"
newnewstr= "파이썬은,하하하,호호호,히히히,파이썬은,파이썬은,파이썬은"
print(newnewstr.split(","))
'''
print(2,"+",3,"=",5)
print('{}+{}={}'.format(2,3,5))

a,b=5,10.0000
print('{}+{}={}'.format(a,b,a+b))
print('{0}+{1}={2}'.format(a,b,a+b))
print('{0:d}+{1:f}={2:f}'.format(a,b,a+b))
print('{0:d}+{1:f}={2:f},{3:s}'.format(a,b,a+b,"gdgdgd"))
'''
'''
print(str.find ("자바"))
print(str.index("자바"))

print(str.find ("파이썬"))
print(str.find ("파"))
print(str.find ("썬"))
print(str.index("파이썬"))
print(str.index ("파"))
print(str.index ("썬"))
'''
'''
newstr = str.replace("파이썬","자바")
print("str:",str)
print("newstr :",newstr)

print("str.count('파이썬')",str.count("파이썬"))
print('$$'.join(str))

'''
'''
value = False #True
print(type(value))
print(int(value))

print(bool(0), bool(1),bool(1.1222),bool(-12))
print(bool("dadadata"),bool("-1"),bool(""))
print( 'bool("")',bool(""))

'''


#0404
#if문
'''
if 조건 :
      실행문1
else :      
      실행문2
'''
'''
#오전?  오후
hour = 19

if hour <12 :
    print("12시가 지나지 않았으니까 오전이네요.")
elif hour <18 :
     print("12시가 지나고,18시가 안지났으니 오후입니다.")
else : 
    print("18시가 지나서 저녁입니다.")
'''
#장학금
#score < 200 50만원을 줌
#200 <= score < 400 100만원
# 400 < score <500 1000만원

'''
score_str = input("점수는? ")
score= int(score_str)
if score < 200:
    print("50만원입니다")
elif score <400 :
    print("100만원")
else :
    print("1000만원")

#점심식사

bap = input("서브웨이 먹을래? 먹고싶으면 yes")

if  bap =='yes' :
    print("8호관 1층")
else :
    again_answer = input("학식? 먹고싶으면 yes")
    if again_answer == 'yes' :
        print("8호관 3층")
    else :
        print("먹지마시발")
'''
'''
#반복문
#for

#for(int i=0; i <5 ; i++){
#    print ("aadadad")
#}

for i in 1,3,4,5,6,8 :
    print(i)

for i in range(0,11,5) :
    print(i)

#0,1,2,3....10

print("range1 ")
for i in range(0,11,5) :
    print(i)

print("range2 ")
for i in range(11) :
    print(i)

#1부터 10까지 합을 구하시오.
sum=0
for i in range(11):
    sum+=i
    print(i,"번째 sum은",sum)
    #sum += i
else : 
    print("for문의 조건이 더이상 만족하지 않습니다. ")
    print(" i가 range(11)에서 벗어남")
    print("for문이 break나 countinue로 종료된게 아니라 정상종료시에만 실행 ")
print("sum : " ,sum  )
'''
'''
while 조건 :
    수행문
''' 
'''
i=10
while i>5 :
    print(i,"는 5보다 크다.")
    i -=1
#n=1부터 5까지 찍어보는 프로그래밍
#1 2 3 4 5
i=1
while i<=5 :
    print(i,end = '   **   ')
    i+=1
else:
    print("while이 잘 끝남")
    print("현재 i의 값은 ", i,"입니다")
'''
'''
#놀이기구 탑승
#4명 탑승 가능
#150cm 이상 탑승가능

num = input("몇명인가요")

while num ==4 :
    print("탑승 가능합니다")

else :
    cm_str = input("키가 몇이세요")
    cm= int(cm_str)
    if cm>=150 :
        print("탑승하세요")
    else:
        print("꺼지세요")

people = 0
while people <4: 
    height = input("키는?")
    int_height = int(height)
    if int_height >150 :
        people+=1
        print("한명 더 탑승")
        print("현재 인원 : ",people)
    else:
        print("못타요")
else:
    print("완료. 놀이이구 시작")
'''
#continue, break
#반복문 중간에 반복을 더이상하지 않고 실행을 종료
#반복문 안쪽에서 실행된다.
#주로 if문 안쪽에서 사용됨

#input으로 입력받는데
#무한반복
#exit이라는 값을 받으면, 입력받는것을 종료.

while True:
    str = input("단어를 입려받으세요.")
    if str == "exit":
        print("종료여")
        break
    else:
        if str=="apple":
            print("apple을 입력받았음")
            print("continue실행함")
            continue
        print("단어를 입력했습니다",str)
    print("저는 아직 while안에 있어요.")
print("while이 종료됨")