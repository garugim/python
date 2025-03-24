print("Hello, World!")
print("안녕 파이썬")
# 구구단 프로그램 (숫자 입력 검사 추가)

while True:
    num = input("출력할 구구단을 입력하세요: ")

    if num.isdigit():  # 입력값이 숫자인지 확인
        num = int(num)
        print(f"{num}단 출력:")
        for i in range(1, 10):
            print(f"{num} × {i} = {num * i}")
        break  # 정상적인 입력이면 반복문 종료
    else:
        print("유효한 숫자를 입력해주세요.")  # 숫자가 아니면 경고 메시지 출력
