#treehit = 0
#while treehit < 10:
 #   treehit = treehit +1
  #  print("나무를 %d번 찍었습니다" % treehit)
   # if treehit == 10:
    #    print("나무 넘어갑니다")

while True:
    print("그림 출력 프로그램")
    print("~~~~~~~~~~~~~~~~")
    print("1. 큰 2022")
    print("2. 고양이")
    print("3. 경례 이모티콘")
    print("~~~~~~~~~~~~~~~~")
    print("0. 프로그램 종료")
    v = int(input("선택: "))

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

        # ctrl+c 강제 브레이크