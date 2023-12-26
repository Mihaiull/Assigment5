from colorama import Fore, Back, Style
from os import system
from time import sleep
from PatientClass import Patient
from SortingFuncs import srt
#departament class that has id, name, number of beds, and a list of patients
class Departament:
    def __init__(self, id, name, numberOfBeds):
        self.__id = id
        self.__name = name
        self.__numberOfBeds = numberOfBeds
        self.__patients = []
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def numberOfBeds(self):
        return self.__numberOfBeds
    @property
    def patients(self):
        return self.__patients
    
    @id.setter
    def setId(self, id):
        self.__id = id
    @name.setter
    def setName(self, name):
        self.__name = name
    @numberOfBeds.setter
    def setNumberOfBeds(self, numberOfBeds):
        self.__numberOfBeds = numberOfBeds
    @patients.setter
    def addPatient(self, patient):
        if type(patient) == Patient:
            if len(self.__patients) < self.__numberOfBeds:
                self.__patients.append(patient)
            else:
                raise Exception("There are no more beds available!")
        if type(patient) == list:
            for pacient in range(len(patient)):
                if len(self.__patients) < self.__numberOfBeds:
                    self.__patients.append(pacient)
                else:
                    raise Exception("There are no more beds available!")                    
    #sort the patients by personal numerical code:
    def sortPatientsByCode(self):
        srt(self.patients, key=lambda patient: patient.code)
    
    def minimalPrint(self):
        return f"{Fore.GREEN}Departament Id: {Fore.WHITE}{self.__id}{Fore.GREEN} Name: {Fore.WHITE}{self.__name}{Fore.GREEN} Number of beds: {Fore.WHITE}{self.__numberOfBeds}{Style.RESET_ALL}"

    def __str__(self):
        frumusete = ' '.join([str(patient) for patient in self.__patients])
        return f"{Fore.GREEN}Departament Id: {Fore.WHITE}{self.__id}{Fore.GREEN} Name: {Fore.WHITE}{self.__name}{Fore.GREEN} Number of beds: {Fore.WHITE}{self.__numberOfBeds}\n{Fore.GREEN}Patients:\n {Fore.WHITE}{frumusete}{Style.RESET_ALL}"
    def __repr__(self):
        return str(self)
    
if __name__ == "__main__":
    print("This module is not meant to be run by itself!")
    from main import main
    main()