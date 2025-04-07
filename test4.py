# 함수 만들기
def hello():
    print("hello world")

# 함수 호출(실행)
hello()

def hello_name(name):
    print (f"안녕 {name}야!")
name = input("이름을 입력:")
hello_name(name)
    

def cal(n1, n2, op):
    r = 0  # 결과값
    if op == "+":
        r = n1 + n2  # 변수 이름 수정: ni -> n1
    elif op == "-":
        r = n1 - n2  # 이 부분에 빼기 연산 추가
    else:
        print("잘못입력")
    return r

r = cal(2, 1, "+")
print(f"두 수를 더한 값: {r}")  # f-string으로 변수 값 출력

r = cal(2, 1, "-")
print(f"두 수를 뺀 값: {r}")  # 'peint' 오타를 'print'로 수정

#