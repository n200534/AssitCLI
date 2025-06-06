from rich.console import Console
from rich.markdown import Markdown
from assistant.gemini_client import generate_text_with_gemini

console = Console()

def translate_code(code: str, target_language: str) -> None:
    prompt = f"Detect the language and Translate the following  into {target_language}:\n\n{code}\n\nTranslated Code:"
    try:
        translation = generate_text_with_gemini(prompt)
        console.print(Markdown(translation))
    except Exception as e:
        console.print(f"[bold red]Error calling Gemini API:[/bold red] {e}")
