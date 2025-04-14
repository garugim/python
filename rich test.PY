from rich.console import Console
from rich.style import Style
from rich.text import Text
from rich.panel import Panel

console = Console()

def print_font_designs():
    # 기본적인 스타일 출력
    console.print("[bold red]굵고 빨간 텍스트[/bold red]")
    console.print("[italic green]이탤릭 녹색 텍스트[/italic green]")
    console.print("[underline blue]밑줄이 있는 파란 텍스트[/underline blue]")
    console.print("[bold underline magenta]굵고 밑줄이 있는 자홍색 텍스트[/bold underline magenta]")
    
    # Text 클래스를 이용한 스타일 설정
    styled_text = Text("Rich 라이브러리로 만든 멋진 텍스트!", style=Style(color="cyan", bold=True, italic=True))
    console.print(styled_text)
    
    # Panel을 이용한 꾸며진 텍스트 박스
    panel = Panel("Panel 내부 텍스트", title="멋진 Panel", subtitle="서브타이틀")
    console.print(panel)
    
    # blink 스타일 (터미널에 따라 지원하지 않을 수 있음)
    console.print("[blink bold yellow]깜빡이며 굵은 노란 텍스트[/blink bold yellow]")
    
    # 더 복잡한 텍스트 디자인을 위한 마크업도 사용 가능
    console.print(
        "[bold red]Bold[/bold red] + [italic green]Italic[/italic green] + "
        "[underline blue]Underline[/underline blue] = 멋진 조합!"
    )

if __name__ == "__main__":
    print_font_designs()
