import os
from rich.console import Console

console = Console()

def pause(message:str="Enter to continue..."):
    console.print(message, style="cyan")
    input()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def status_message(title:str, response):
    return {"title":title, "response":response}