from DepartamentClass import Departament
from PatientClass import Patient
from colorama import Fore, Back, Style
from os import system
from time import sleep

#hospital class(which is actually a departament repository) that has a list of departaments
class hospital:
    def __init__(self):
        self.__departaments = []
    @property
    def departaments(self):
        return self.__departaments
    @departaments.setter
    def addDepartament(self, departament):
        self.__departaments.append(departament)
    #sort departaments by number of patients
    def sortDepsNOP(self):
        pass
    #sort departaments by patients having the age above a cet