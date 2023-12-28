from DepartamentClass import Departament
from PatientClass import Patient
from colorama import Fore, Style
from SortingFuncs import srt, flt, srch

#hospital class(which is actually a departament repository) that has a list of departaments
class Hospital:
    def __init__(self):
        self.__departaments = []
    @property
    def departaments(self):
        return self.__departaments
    @departaments.setter
    def addDepartament(self, departament):
        self.__departaments.append(departament)

    #print only departaments
    def printDeps(self):
        for i in range(len(self.departaments)):
            print(self.departaments[i].minimalPrint())

    #remove a patient from a departament
    def removePatient(self, depindex, code):
        for i in range(len(self.departaments[depindex].patients)):
            if self.departaments[depindex].patients[i].code == code:
                del self.departaments[depindex].patients[i]
                return f"{Fore.GREEN}'Patient removed successfully!'{Style.RESET_ALL}"
        return f"{Fore.RED}'Patient not found!'{Style.RESET_ALL}"
    
    #remove a departament from the list of departaments
    def removeDepartament(self, id):
        for departament in self.departaments:
            if departament.id == id:
                self.departaments.remove(departament)
                return
        raise Exception("Departament not found!")
    
    #sort departaments by number of patients
    def sortDepsNOP(self):
        srt(self.departaments, key=lambda dep: len(dep.patients), reverse=True)

    #sort departaments by patients having the age above a certain value
    def sortDepsAge(self, age):
        srt(self.departaments, key=lambda dep:len(srch(dep.patients, key=lambda patient: patient.age >= age)))

    #sort departaments by number of patients and sort the patients in each departament alphabetically
    def sortuVietiiMele(self):
        #already have a function for the first half
        self.sortDepsNOP()
        #sort the patients in each departament alphabetically
        for i in range(len(self.departaments)):
            srt(self.departaments[i].patients, key=lambda patient: patient.lastName[0])
        
    #identify departaments which containes patiens under a given age
    def filterDepsAge(self, age):
        return flt(self.departaments, key=lambda dep: len(srch(dep.patients, key=lambda patient: patient.age < age)))
    
    #indentify patients from a given departament which contain a given string in their firstName or lastName
    def searchPatients(self, depId, string):
        return srch(self.departaments[depId].patients, key=lambda patient: string in patient.firstName or string in patient.lastName)
    
    #indentify departaments which contain patients with a given first name
    def filterDepsName(self, firstName):
        return flt(self.departaments, key=lambda dep: len(srch(dep.patients, key=lambda patient: firstName == patient.firstName)))
    
    #form groups of k patiens from the same departaments and the same disease(k is given):
    def formKGroupsInEachDep(self, k):
        printedlist = []
        for i in range(len(self.departaments)):
            for j in range(len(self.departaments[i].patients)):
                if len(self.departaments[i].patients[j].disease) == k:
                    printedlist.append(f"{Fore.GREEN}Group {Fore.WHITE}{j//k+1}{Fore.GREEN} from departament {Fore.WHITE}{self.departaments[i].name}{Fore.GREEN}:\n{Fore.WHITE}{self.departaments[i].patients[j:j+k]}")
        return printedlist
    
    #form groups of k departaments having at most p patients that suffer from the same disease(k and p are given)
    def formKGroupsInEachDepCuP(self, k, p):
        printedlist = []
        for i in range(0, len(self.departaments), k):
            for j in range(len(self.departaments[i].patients)):
                if len(self.departaments[i].patients[j].disease) <= p:
                    printedlist.append(f"{Fore.GREEN}Group {Fore.WHITE}{j//k+1}{Fore.GREEN} from departament {Fore.WHITE}{self.departaments[i].name}{Fore.GREEN}:\n{Fore.WHITE}{self.departaments[i].patients[j:j+k]}")
            return printedlist
        
    #may god have mercy on the fuckery that the last 6 functions are
        
    def __str__(self):
        return f" {' '.join(str(departament) for departament in self.departaments)}"
    
if __name__ == "__main__":
    print("This module is not meant to be run by itself!")
    from main import main
    main()