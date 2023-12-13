from colorama import Fore, Back, Style
from os import system
from time import sleep
from PatientClass import Patient

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
    #for mass adding patients in testing
    @patients.setter
    def setPatients(self, patients):
        self.__patients.clear()
        self.__patients = patients[:]
    #add a patient to the list of patients
    @patients.setter
    def addPatient(self, patient):
        if len(self.patients) < self.numberOfBeds:
            self.__patients.append(patient)
        else:
            raise Exception("The departament is full!")
    #remove a patient from the list of patients
    @patients.setter
    def removePatient(self, patient):
        self.__patients.remove(patient)
    #remove all patients from the list of patients
    @patients.setter
    def removeAllPatients(self):
        self.__patients.clear()
    
    #sort the patients by personal numerical code:
    def sortPatientsByCode(self):
        self.__patients.sort(key=lambda patient: patient.code)


    def __str__(self):
        return f"{Fore.GREEN}Id: {Fore.WHITE}{self.__id}\n{Fore.GREEN}Name: {Fore.WHITE}{self.__name}\n{Fore.GREEN}Number of beds: {Fore.WHITE}{self.__numberOfBeds}\n{Fore.GREEN}Patients: {Fore.WHITE}{self.__patients} {Style.RESET_ALL}"
    def __repr__(self):
        return str(self)