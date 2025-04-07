def print_ascii_art():
    art = """┏┓┏┓┏┓┏┓ 
┏┛┃┃┏┛┏┛ 
┗┛┗┛┗┛┗┛"""
    print(art)

# 사용자로부터 입력 받기
user_input = input("숫자를 입력하세요: ")

if user_input == "1":
    print_ascii_art()