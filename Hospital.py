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
        #departaments with the most patiens first, then the rest
        #for some reason the sorter doesn't work so manual sort it is
        #srt(self.departaments, key=lambda dep: len(srch(dep.patients, key=lambda patient: patient.age < age)), reverse=True)
        for i in range(len(self.departaments)):
            for j in range(i,len(self.departaments)):
                if len(srch(self.departaments[i].patients, key=lambda patient: patient.age < age)) > len(srch(self.departaments[j].patients, key=lambda patient: patient.age < age)):
                    self.departaments[i], self.departaments[j] = self.departaments[j], self.departaments[i]
    #indentify patients from a given departament which contain a given string in their firstName or lastName
    def searchPatients(self, depId, string):
        return srch(self.departaments[depId].patients, key=lambda patient: string in patient.firstName or string in patient.lastName)
    
    #indentify departaments which contain patients with a given first name
    def filterDepsName(self, firstName):
        return flt(self.departaments, key=lambda dep: len(srch(dep.patients, key=lambda patient: firstName == patient.firstName)))
    
    #form groups of k patiens from the same departaments and the same disease(k is given):
    def backtracking_group_k(self, k:int, index=0, group=[], groups=[]):
        departaments = self.departaments
        if len(group) == k:
            groups.append(group[:])
            return
        for i in range(index, len(departaments)):
            for j in range(len(departaments[i].patients)):
                if departaments[i].patients[j].disease == departaments[index].patients[0].disease:
                    group.append(departaments[i].patients[j])
                    self.backtracking_group_k(k, i+1, group, groups)
                    group.pop()
        return groups

    #form groups of k departaments having at most p patients that suffer from the same disease(k and p are given)
    def backtracking_group_k_p(self, k:int, p:int, index=0, group=[], groups=[]):
        departaments = self.departaments
        if len(group) == k:
            groups.append(group[:])
            return
        for i in range(index, len(departaments)):
            if len(departaments[i].patients) <= p:
                if len(group) > 0:
                    if departaments[i].patients[0].disease == group[0].patients[0].disease:
                        group.append(departaments[i])
                        self.backtracking_group_k_p(k, p, i+1, group, groups)
                        group.pop()
        return groups
        
    #may god have mercy on the fuckery that the last 2 functions are
        
    def __str__(self):
        return f" {' '.join(str(departament) for departament in self.departaments)}"
    
if __name__ == "__main__":
    print("This module is not meant to be run by itself!")
    from main import main
    main()

#5030628410020