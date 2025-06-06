from rich.console import Console
from rich.markdown import Markdown
from assistant.gemini_client import generate_text_with_gemini

console = Console()

def debug_code(code: str, error_message: str) -> None:
    prompt = f"Help debug the following Python code. The code produces this error: {error_message}\n\nCode:\n{code}\n\nProvide an explanation and debugging steps in markdown:"
    try:
        debug_info = generate_text_with_gemini(prompt)
        console.print(Markdown(debug_info))
    except Exception as e:
        console.print(f"[bold red]Error calling Gemini API:[/bold red] {e}")
