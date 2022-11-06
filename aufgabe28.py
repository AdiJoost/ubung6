import re

def getUserInput() -> str:
    return input("Geben Sie eine User ID ein(q to quit): ")

def checkUserInput(userInput: str, firstCase=True) -> re.Match[str]:
    pattern1 = re.compile("[A-Z]{1,3}[0-9]{5}")
    pattern2 = re.compile("[A-Z]{2}\d")
    return pattern1.fullmatch(userInput) if firstCase else pattern2.fullmatch(userInput)

while True:
    userInput = getUserInput()
    if userInput == "q":
        print("Ihre Eingabe 'q' entspricht keinem Vorgegebenen Pattern")
        break
    print("Ihre Eingabe hat 1-3 Grossbuchstaben gefolgt von genau 5 Ziffern? "+ 
        ("True" if checkUserInput(userInput) else "False"))
    
    print("Ihre Eingabe hat genau 2 Grossbuchstaben gefolgt von genau 1 Ziffer? "+ 
        ("True" if checkUserInput(userInput, firstCase=False) else "False"))
