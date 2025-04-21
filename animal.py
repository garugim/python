from rich.console import Console
from rich.table import Table
from PIL import Image
import os, sys

console = Console()

def display_menu_table(include_exit: bool = False):
    table = Table(
        title="[bold cyan]그림 출력 프로그램[/bold cyan]",
        show_header=True,
        header_style="bold green"
    )
    table.add_column("번호", justify="center", style="bold yellow")
    table.add_column("항목", justify="center", style="bold magenta")
    table.add_row("1", "강아지 보기")
    table.add_row("2", "고양이 보기")
    table.add_row("3", "경례 보기")
    if include_exit:
        table.add_row("0", "프로그램 종료")
    console.print(table)

def show_image(path: str):
    """Pillow Image.show()로 운영체제 기본 뷰어에서 이미지를 엽니다."""
    if not os.path.isfile(path):
        console.print(f"[red]❌ 이미지 파일을 찾을 수 없습니다: {path}[/red]")
        return
    try:
        img = Image.open(path)
    except Exception as e:
        console.print(f"[red]❌ 이미지를 열 때 오류 발생: {e}[/red]")
        return

    console.print(f"[green]이미지를 기본 뷰어로 열고 있습니다...[/green]")
    img.show()

def play_menu(include_exit: bool):
    """한 사이클 메뉴를 한 번 실행"""
    display_menu_table(include_exit)
    try:
        choice = int(input("선택: "))
    except ValueError:
        console.print("[bold red]숫자를 입력해주세요![/bold red]")
        return False  # 사이클 끝, 다음 반복

    if choice == 1:
        show_image("dog.png")
    elif choice == 2:
        show_image("cat.png")
    elif choice == 3:
        show_image("salute.png")
    elif choice == 0 and include_exit:
        console.print("[bold red]프로그램을 종료합니다[/bold red]")
        return True   # 종료 플래그
    else:
        console.print("[red]잘못 입력하셨습니다[/red]")

    return False  # 계속

def main():
    # 1) 처음에 5번 반복 (종료 옵션 없음)
    console.print("[bold underline green]== 다섯 번 반복 (exit 옵션 없음) ==[/]")
    for i in range(5):
        console.print(f"[dim]— {i+1}번째 실행 —[/dim]")
        play_menu(include_exit=False)

    # 2) 이후 무한 반복 (0 입력 시 종료)
    console.print("[bold underline green]== 무한 반복 (0 입력 시 종료) ==[/]")
    while True:
        should_exit = play_menu(include_exit=True)
        if should_exit:
            break

if __name__ == "__main__":
    main()

