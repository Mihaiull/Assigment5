from UI import UI
from time import sleep
from colorama import Fore, Style

def main():
    try:
        UI()
    except ValueError as ve:
        print(ve)
        UI()
    except Exception as ex:
        print(ex)
        UI()

if __name__ == "__main__":
    main()