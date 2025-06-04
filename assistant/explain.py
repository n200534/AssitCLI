from rich.console import Console
from rich.markdown import Markdown
from assistant.gemini_client import generate_text_with_gemini

console = Console()

def explain_code(code: str) -> None:
    prompt = f"Explain the following Python code in simple terms using markdown:\n\n{code}\n\nExplanation:"
    try:
        explanation = generate_text_with_gemini(prompt)
        # Render explanation as markdown in terminal
        console.print(Markdown(explanation))
    except Exception as e:
        console.print(f"[bold red]Error calling Gemini API:[/bold red] {e}")
