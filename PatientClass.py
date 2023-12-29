from colorama import Fore, Style
from datetime import date

def calc_age(codes):
    code = str(codes)
    dates = int(date.today().year)
    if int(code[0:]) < 3:
        return dates - int("19" + str(code[1:3]))
    else:
        return dates - int("20" + str(code[1:3]))

#a patient class that has first name, last name, personal numerical code, and disease
class Patient:
    def __init__(self, firstName, lastName, code, disease):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__code = code
        self.__disease = disease
        self.__age = calc_age(self.__code)
    @property
    def firstName(self):
        return self.__firstName
    @property
    def lastName(self):
        return self.__lastName
    @property
    def code(self):
        return self.__code
    @property
    def disease(self):
        return self.__disease
    @property
    def age(self):
        return self.__age
    
    @firstName.setter
    def setFirstName(self, firstName):
        self.__firstName = firstName
    @lastName.setter 
    def setLastName(self, lastName):
        self.__lastName = lastName
    @code.setter
    def setCode(self, code):
        self.__code = code
    @disease.setter
    def setDisease(self, disease):
        self.__disease = disease

    def __str__(self):
        #printer = ' '.join(list)
        return f"{self.__firstName} {self.__lastName} {Fore.BLUE} {self.__code} {Fore.RED} {self.__disease}{Style.RESET_ALL}\n"

    def __repr__(self):
        return str(self)
    
if __name__ == "__main__":
    print("This module is not meant to be run by itself!")
    from main import main
    main()