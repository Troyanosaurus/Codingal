from textblob import TextBlob
import colorama
import time

def show_proccessing_animation():
    for i in range(3):
        print(".")
        time.sleep(1)


def analyze_sentiment(text):
    p = TextBlob(text).sentiment.polarity
    if p > 0.25:
        p = "Positive"
    elif p < -0.25:
        p = "Negative"
    else:
        p = "Neutral"

    print(f"Sentiment: {p}")



def execute_command(command):
    pass
# I don't know how to do it, because I already put all the if statements in and it works fine.

def get_valid_name():
    while True:
        name = input("Hello user whats your name?\n")
        if name.isalpha():
            print("Nice to meet you", name)
            return name

        else:
            print("Invalid name")

history = {}
get_valid_name()


while True:
    sentence = input(f"Please type a sentence for sentiment analysis\n").lower().strip()
    if sentence == "help":
        print("summary | reset | history | help | exit")

    elif sentence == "summary":
        print("HELP")

    elif sentence == "reset":
        history.clear()
        print("History cleared.")

    elif sentence == "history":
        if history != {}:
            for sent, value in history:
                print(f"{sent} : {value}")
        else:
            print("No history yet")

    elif sentence == "exit":
        with open(f"{name}_sentiment_analysis.txt", "w") as file:
            for sent, value in history:
                file.write(f"{sent} : {value}\n")

    else:
        show_proccessing_animation()
        analyze_sentiment(sentence)
