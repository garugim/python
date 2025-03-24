# 구구단 프로그램

num = int(input("출력할 구구단을 입력하세요: "))

print(f"{num}단 출력:")
for i in range(1, 10):
    print(f"{num} × {i} = {num * i}")
