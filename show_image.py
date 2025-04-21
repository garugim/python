from PIL import Image
import os, sys

def main():
    image_path = "input.jpg"  # 스크립트와 같은 폴더에 있어야 합니다.
    if not os.path.isfile(image_path):
        print(f"❌ 이미지 파일을 찾을 수 없습니다: {image_path}")
        sys.exit(1)

    # 이미지 열기
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"❌ 이미지를 열 때 오류 발생: {e}")
        sys.exit(1)

    # 사용자에게 알림
    print("이미지를 기본 뷰어로 열어봅니다...")
    # 윈도우의 사진 뷰어(또는 연결된 프로그램) 로 자동 실행
    img.show()

if __name__ == "__main__":
    main()