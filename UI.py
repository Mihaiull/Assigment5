from Hospital import Hospital
from PatientClass import Patient
from DepartamentClass import Departament
from os import system
from colorama import Fore, Style
from time import sleep

def menu():
    #de ce sa am 17 printuri can pot sa am doar 1
    print(f"{Fore.YELLOW}0.Exit\n1. Add a departament\n2. Remove a departament\n3. Add a patient\n4. Remove a patient\n5. Display departaments\n6. Display patients\n7. Sort departaments by number of patients\n8. Sort departaments by patients having the age above a certain value\n9. Sort departaments by number of patients and sort the patients in each departament alphabetically\n10. Identify departaments which containes patiens under a given age\n11. Indentify patients from a given departament which contain a given string in their firstName or lastName\n12. Indentify departaments which contain patients with a given first name\n13. Form groups of k patiens from the same departaments and the same disease(k is given)\n14. Form groups of k departaments having at most p patients that suffer from the same disease(k and p are given)\n{Style.RESET_ALL}")

#option_dict = { 0: exit, 1: "departaments(x)", 2: "removeDepartament", 3: "addPatient", 4: "removePatient", 5: "displayDepartaments", 6: "displayPatients", 7: "sortDepsNOP", 8: "sortDepsAge", 9: "sortuVietiiMele", 10: "filterDepsAge", 11: "searchPatients", 12: "filterDepsName", 13: "formKGroupsInEachDep", 14: "formKGroupsInEachDep"}

def UI():
    hospital = Hospital()
    #some pre added departaments and patients for testing
    hospital.departaments.append(Departament(1, "Cardiology", 10))
    hospital.departaments[len(hospital.departaments)-1].patients.append(Patient("John", "Doe", 123456789, "Heart attack", 45))
    while(True):
        menu()
        option = int(input("Choose an option: "))
        if option == 0:
            break
        elif option == 1:
            system("cls||clear")
            id = int(input("Id: "))
            name = input("Name: ")
            numberOfBeds = int(input("Number of beds: "))
            hospital.departaments(Departament(id, name, numberOfBeds))
            system("cls||clear")
            print("Do you also want to add patients to this departament?")
            option2 = input("y/n:")
            if option2 == "y":
                system("cls||clear")
                numberOfPatients = int(input("Number of patients: "))
                for i in range(numberOfPatients):
                    print (f"Patient {i+1}:")
                    firstName = input("First name: ")
                    lastName = input("Last name: ")
                    code = int(input("Code: "))
                    disease = input("Disease: ")
                    age = int(input("Age: "))
                    hospital.departaments[len(hospital.departaments)-1].patients(Patient(firstName, lastName, code, disease, age))
                    system("cls||clear")
            if option2 == "n":
                system("cls||clear")
                continue
            print(f"{Fore.GREEN}Departament added successfully!{Style.RESET_ALL}")
            sleep(1)
            system("cls||clear")
        

        print(hospital)




if __name__ == "__main__":
    print("This module is not meant to be run by itself!")
    UI()
    input("Press any key to continue...")
    exit()