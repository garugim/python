# 만약에 입력받은 값이 0이면 0이다
v = int(input("입력값:"))

# v가 숫자인지 문자열인지 알고 싶을 때 사용하는 방법
#print(type(v)) 
#print("숫자로 변환")
#v = int(v)
#print(type(v))

# if v -- "0" # 문자열로 비교 
#if v == 0: # 숫자로 비교
    #print("0이다")
# 만약에 입력받은 값이 0이 아니면 0이 아니다
#if v != 0:
    #print("0이 아니다")
    
# 만약에 입력받은 값이 0이면 0이다를 출력 아니면 0이 아니다를 출력
if v == 0: # 숫자로 비교
    print("0이다")
else:
    print("0이아니다")