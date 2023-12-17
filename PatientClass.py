from colorama import Fore, Style

#a patient class that has first name, last name, personal numerical code, and disease
class Patient:
    def __init__(self, firstName, lastName, code, disease):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__code = code
        self.__disease = disease
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
        return f"{Fore.GREEN}First Name: {Fore.WHITE}{self.__firstName}\n{Fore.GREEN}Last Name: {Fore.WHITE}{self.__lastName}\n{Fore.GREEN}Personal Code: {Fore.WHITE}{self.__code}\n{Fore.GREEN}Disease: {Fore.WHITE}{self.__disease} {Style.RESET_ALL}"
    def __repr__(self):
        return str(self)
    