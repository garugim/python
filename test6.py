from rich.console import Console
from rich.table import Table

console = Console()

def display_menu_table(include_exit=False):
    # Table 생성: 제목과 헤더 스타일 지정
    table = Table(title="[bold cyan]그림 출력 프로그램[/bold cyan]", show_header=True, header_style="bold green")
    
    # 컬럼 추가: 번호와 항목
    table.add_column("번호", justify="center", style="bold yellow")
    table.add_column("항목", justify="center", style="bold magenta")
    
    # 메뉴 옵션 추가
    table.add_row("1", "큰 2022")
    table.add_row("2", "고양이")
    table.add_row("3", "경례 이모티콘")
    
    # 종료 옵션 추가 (필요한 경우)
    if include_exit:
        table.add_row("0", "프로그램 종료")
    
    # 테이블 출력
    console.print(table)

def play_game_1():
    for _ in range(5):
        # 메뉴 출력 (종료 옵션 없음)
        display_menu_table()
        
        # 입력값을 정수로 변환
        try:
            choice = int(input("선택: "))
        except ValueError:
            console.print("[bold red]숫자를 입력해주세요![/bold red]")
            continue

        if choice == 1:
            console.print("[bold red]큰 2022[/bold red]")
            console.print("[bold red]┏┓┏┓┏┓┏┓[/bold red]")
            console.print("[bold red]┏┛┃┃┏┛┏┛[/bold red]")
            console.print("[bold underline red]┗┛┗┛┗┛┗┛[/bold underline red]")
        elif choice == 2:
            console.print("[bold magenta]고양이 그림[/bold magenta]")
            console.print(" ^ _ ^ ")
            console.print("( o.o )")
            console.print(" > ^ < ")
        elif choice == 3:
            console.print("[bold cyan]경례 이모티콘[/bold cyan]")
            console.print("[italic yellow]/(ovo)>[/italic yellow]")
        else:
            console.print("[red]잘못 입력하셨습니다[/red]")

def play_game_2():
    while True:
        # 메뉴 출력 (종료 옵션 포함)
        display_menu_table(include_exit=True)
        
        # 입력값을 정수로 변환
        try:
            choice = int(input("선택: "))
        except ValueError:
            console.print("[bold red]숫자를 입력해주세요![/bold red]")
            continue

        if choice == 1:
            console.print("[bold red]큰 2022[/bold red]")
            console.print("[bold red]┏┓┏┓┏┓┏┓[/bold red]")
            console.print("[bold red]┏┛┃┃┏┛┏┛[/bold red]")
            console.print("[bold underline red]┗┛┗┛┗┛┗┛[/bold underline red]")
        elif choice == 2:
            console.print("[bold magenta]고양이 그림[/bold magenta]")
            console.print(" ^ _ ^ ")
            console.print("( o.o )")
            console.print(" > ^ < ")
        elif choice == 3:
            console.print("[bold cyan]경례 이모티콘[/bold cyan]")
            console.print("[italic yellow]/(ovo)>[/italic yellow]")
        elif choice == 0:
            console.print("[bold red]프로그램을 종료합니다[/bold red]")
            break
        else:
            console.print("[red]잘못 입력하셨습니다[/red]")

# 프로그램 실행
play_game_1()
play_game_2()
