import colorama
from colorama import Fore as F, Style
from textblob import TextBlob

colorama.init()
print(f"{F.CYAN} Welcome to Sentiment Spy! {Style.RESET_ALL}")
name = input(f"{F.MAGENTA}Name: {Style.RESET_ALL}").strip() or "Mystery Agent"
h = []

while 1:
    x = input(f"{F.GREEN}>> {Style.RESET_ALL}").strip()
    if not x:
        print(f"{F.RED}Enter some text!{Style.RESET_ALL}")
        continue
    c = x.lower()

    if c == "exit":
        print(f"Bye, Agent {name}! [emoji]")
        break
    if c == "reset":
        h.clear()
        print("History cleared!")
        

