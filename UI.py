from Hospital import Hospital
from PatientClass import Patient
from DepartamentClass import Departament
from os import system
from colorama import Fore, Style
from time import sleep

def menu():
    #de ce sa am 17 printuri can pot sa am doar 1
    print(f"{Fore.YELLOW}0.Exit\n1. Add a departament\n2. Remove a departament\n3. Add a patient\n4. Remove a patient\n5. Display departaments\n6. Display patients\n7. Sort departaments by number of patients\n8. Sort departaments by patients having the age above a certain value\n9. Sort departaments by number of patients and sort the patients in each departament alphabetically\n10. Identify departaments which containes patiens under a given age\n11. Indentify patients from a given departament which contain a given string in their firstName or lastName\n12. Indentify departaments which contain patients with a given first name\n13. Form groups of k patiens from the same departaments and the same disease(k is given)\n14. Form groups of k departaments having at most p patients that suffer from the same disease(k and p are given)\n{Style.RESET_ALL}")

option_dict = { 0: exit, 1: "departaments(x)", 2: "removeDepartament", 3: "addPatient", 4: "removePatient", 5: "displayDepartaments", 6: "displayPatients", 7: "sortDepsNOP", 8: "sortDepsAge", 9: "sortuVietiiMele", 10: "filterDepsAge", 11: "searchPatients", 12: "filterDepsName", 13: "formKGroupsInEachDep", 14: "formKGroupsInEachDep"}

def UI():
    hospital = Hospital()
    #some pre added departaments and patients for testing
    hospital.departaments(Departament(1, "Cardiology", 7))
    hospital.departaments[0].patients(Patient("Ion", "Popescu", 1234567890123, "fomist"), Patient("Vasile", "Ionescu", 1234567890124, "drogangiu"), Patient("Gheorghe", "Popescu", 1234567890125, "fortnite enjoyer"), Patient("Gabi", "Hanu", 69420, "utilizeaza arch linux") , Patient("Ion", "Ionescu", 1234567890126, "face UI cu while"), Patient("Vasile", "Popescu", 1234567890127, "face program de spital inchipuit"))
    hospital.departaments(Departament(2, "Neurology", 7))
    hospital.departaments(Departament(3, "Oncology", ))
    hospital.departaments(Departament(4, "Orthopedics", 3))
    hospital.departaments(Departament(5, "Pediatrics", 3))
    hospital.departaments(Departament(6, "Surgery", 3))
    hospital.departaments(Departament(7, "Urology", 3))
    hospital.departaments(Departament(8, "Ophthalmology", 3))
    menu()
    option = int(input("Choose an option: "))
    
    








if __name__ == "__main__":
    print("This module is not meant to be run by itself!")
    UI()
    input("Press any key to continue...")
    exit()