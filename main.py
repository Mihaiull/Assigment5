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
    string = ['N', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o', 'n', 'i', 'n', 'o']
    for i in range(len(string)):
        if i%2==0:
            sleep(0.005)
            print(Fore.LIGHTBLUE_EX + string[i] + Style.RESET_ALL, end="")
        else:
            sleep(0.005)
            print(Fore.LIGHTRED_EX + string[i] + Style.RESET_ALL, end="")
    sleep(1)
    main()