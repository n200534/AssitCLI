from rich.console import Console
from rich.markdown import Markdown
from assistant.gemini_client import generate_text_with_gemini

console = Console()

def generate_testcases(function_code: str) -> None:
    prompt = f"Generate comprehensive test cases for the following Python function. Provide input-output pairs and explanations in markdown:\n\n{function_code}\n\nTest Cases:"
    try:
        testcases = generate_text_with_gemini(prompt)
        console.print(Markdown(testcases))
    except Exception as e:
        console.print(f"[bold red]Error calling Gemini API:[/bold red] {e}")
