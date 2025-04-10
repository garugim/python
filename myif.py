# 아스키 코드 그림 출력 하기
# 만약에 1을 입혁하면 1번 캐릭터 출력
# 만약에 2를 입력하면 2번 캐릭터 출력
# 3을 입렵하면 3번 캐릭터 출력
# 잘못입력하면 잘못 입렷했다고 출력

def play_game_1():
    for v in range(5):
        print("5번 반복하는 그림 출력 프로그램")
        print("~~~~~~~~~~~~~~~~")
        print("1. 큰 2022")
        print("2. 고양이")
        print("3. 경례 이모티콘")
        print("~~~~~~~~~~~~~~~~")
        
        # 입력값을 정수로 변환
        try:
            v = int(input("선택: "))
        except ValueError:
            print("숫자를 입력해주세요!")
            continue

        if v == 1:
            print("큰 2022")
            print("┏┓┏┓┏┓┏┓")
            print("┏┛┃┃┏┛┏┛")
            print("┗┛┗┛┗┛┗┛")
        elif v == 2:
            print("고양이 그림")
            print(" ^ _ ^ ")
            print("( o.o )")
            print(" > ^ < ")
        elif v == 3:
            print("경례 이모티콘")
            print("/(ovo)>")
        else:
            print("잘못 입력하셨습니다")

def play_game_2():
    while True:
        print("무한히 반복하는 그림 출력 프로그램")
        print("~~~~~~~~~~~~~~~~")
        print("1. 큰 2022")
        print("2. 고양이")
        print("3. 경례 이모티콘")
        print("~~~~~~~~~~~~~~~~")
        print("0. 프로그램 종료")
        
        # 입력값을 정수로 변환
        try:
            v = int(input("선택: "))
        except ValueError:
            print("숫자를 입력해주세요!")
            continue

        if v == 1:
            print("큰 2022")
            print("┏┓┏┓┏┓┏┓")
            print("┏┛┃┃┏┛┏┛")
            print("┗┛┗┛┗┛┗┛")
        elif v == 2:
            print("고양이 그림")
            print(" ^ _ ^ ")
            print("( o.o )")
            print(" > ^ < ")
        elif v == 3:
            print("경례 이모티콘")
            print("/(ovo)>")
        elif v == 0:
            print("프로그램을 종료합니다")
            break
        else:
            print("잘못 입력하셨습니다")


play_game_1()

play_game_2()





# while True: << 이걸로 루프 돌리는게 가장 이상적임

# 그림 출력 프로그램을 총 5번 반복 실행될 수 있게 만드시오.
# 할 수 있는 사람은 프로그램이 계속(무한)반복하게 하고
# 만약에 0을 입력하면 종료되는 프로그램을 만드시오

# 함수를 이용해 두개의 프로그램이 동작 될 수 있게 만들어 보기