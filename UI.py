from Hospital import Hospital
from PatientClass import Patient
from DepartamentClass import Departament
from os import system
from colorama import Fore, Style
from time import sleep
from Generator import generator

def menu():
    #de ce sa am 17 printuri can pot sa am doar 1
    print(f"{Fore.YELLOW}0.Exit\n1. Add a departament\n2. Remove a departament\n3. Add a patient\n4. Remove a patient\n5. Sort departaments by number of patients\n6. Sort departaments by patients having the age above a certain value\n7. Sort departaments by number of patients and sort the patients in each departament alphabetically\n8. Identify departaments which containes patiens under a given age\n9. Indentify patients from a given departament which contain a given string in their firstName or lastName\n10. Indentify departaments which contain patients with a given first name\n11. Form groups of k patiens from the same departaments and the same disease(k is given)\n12. Form groups of k departaments having at most p patients that suffer from the same disease(k and p are given)\n{Style.RESET_ALL}")

hospital = Hospital()
#some pre added departaments and patients for testing
generator(hospital, 5, 5)
def UI():
    try:
        while(True):
            system("cls||clear")
            menu()
            option = input("Choose an option: ")
            if option == '0':
                #exit
                break
            elif option == 'print':
                option2 = input("0. Print all\n3 1. Print departaments\n2. Print patients\n")
                if option2 == '0':
                    print(hospital)
                elif option2 == '1':
                    print(hospital.departaments)
                elif option2 == '2':
                    for i in range(len(hospital.departaments)):
                        print(hospital.departaments[i].patients)
                else:
                    system("cls||clear")
                    raise TypeError("Invalid option!")
            elif option == '1':
                #add a departament
                system("cls||clear")
                id = int(input("Id: "))
                name = input("Name: ")
                numberOfBeds = int(input("Number of beds: "))
                hospital.departaments.append(Departament(id, name, numberOfBeds))
                system("cls||clear")
                print("Do you also want to add patients to this departament?")
                option2 = input("y/n:")
                if option2 == "y":
                    #add patients to the departament
                    system("cls||clear")
                    numberOfPatients = int(input("Number of patients: "))
                    for i in range(numberOfPatients):
                        print (f"Patient {i+1}:")
                        firstName = input("First name: ")
                        lastName = input("Last name: ")
                        code = int(input("CNP: "))
                        disease = input("Disease: ")
                        hospital.departaments[len(hospital.departaments)-1].patients.append(Patient(firstName, lastName, code, disease))
                        system("cls||clear")
                    print(f"{Fore.GREEN}Departament added successfully!{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}Patients added successfully!{Style.RESET_ALL}")
                    sleep(0.5)
                    system("cls||clear")
                if option2 == "n":
                    #don't add patients to the departament
                    system("cls||clear")
                    print(f"{Fore.GREEN}Departament added successfully!{Style.RESET_ALL}")
                    sleep(1)
                    system("cls||clear")
            elif option == '2':
                #remove a departament
                system("cls||clear")
                id = int(input("Enter the id of the departament you want to remove: "))
                hospital.removeDepartament(id)
                system("cls||clear")
                print(f"{Fore.GREEN}Departament removed successfully!{Style.RESET_ALL}")
                sleep(0.3)
                system("cls||clear")
            elif option == '3':
                #add a patient
                system("cls||clear")
                id = int(input("Enter the id of the departament you want to add a patient to: "))
                for i in range(len(hospital.departaments)):
                    if hospital.departaments[i].id == id:
                        system("cls||clear")
                        print(f"{Fore.GREEN}Departament found!{Style.RESET_ALL}\n")
                        print("Input the patient's data:")
                        firstName = input("First name: ")
                        lastName = input("Last name: ")
                        code = int(input("CNP: "))
                        disease = input("Disease: ")
                        hospital.departaments[i].patients.append(Patient(firstName, lastName, code, disease))
                        system("cls||clear")
                        print(f"{Fore.GREEN}Patient added successfully!{Style.RESET_ALL}")
                        sleep(0.3)
                        system("cls||clear")
                        break
            elif option == '4':
                #remove a patient
                system("cls||clear")
                id = int(input("Enter the id of the departament you want to remove a patient from: "))
                for i in range(len(hospital.departaments)):
                    index = -1
                    if hospital.departaments[i].id == id:
                        index = i
                        system("cls||clear")
                        print(f"{Fore.GREEN}Departament found!{Style.RESET_ALL}\n")
                        break
                if index == -1:
                    system("cls||clear")
                    raise Exception("Departament not found!")
                code = int(input("CNP: "))
                print("Input the patient's data:")
                code = int(input("CNP: "))
                for j in range (len(hospital.departaments[index].patients)):
                    if hospital.departaments[index].patients[j].code == code:
                        hospital.departaments[index].patients.pop(j)
                        system("cls||clear")
                        print(f"{Fore.GREEN}Patient removed successfully!{Style.RESET_ALL}")
                        sleep(0.3)
                        system("cls||clear")
                        break
            elif option == '5':
                #sort departaments by number of patients
                system("cls||clear")
                hospital.sortDepsNOP()
                print(f"{Fore.GREEN}Departaments sorted successfully!{Style.RESET_ALL}")
                sleep(0.3)
                system("cls||clear")
            elif option == '6':
                #sort departaments by patients having the age above a certain value
                system("cls||clear")
                age = int(input("Age: "))
                hospital.sortDepsAge(age)
                print(f"{Fore.GREEN}Departaments sorted successfully!{Style.RESET_ALL}")
                sleep(0.3)
                system("cls||clear")
            elif option == '7':
                #sort departaments by number of patients and sort the patients in each departament alphabetically
                system("cls||clear")
                hospital.sortuVietiiMele()
                print(f"{Fore.GREEN}Departaments sorted successfully!{Style.RESET_ALL}")
                sleep(0.3)
                system("cls||clear")
            elif option == '8':
                #identify departaments which containes patiens under a given age
                system("cls||clear")
                age = int(input("Age: "))
                print(f"{Fore.GREEN}Departaments found!{Style.RESET_ALL}\n")
                print(hospital.filterDepsAge(age))
                sleep(0.3)
                system("cls||clear")
            elif option == '9':
                #indentify patients from a given departament which contain a given string in their firstName or lastName
                system("cls||clear")
                id = int(input("Enter the id of the departament you want to search patients in: "))
                string = input("String: ")
                print(f"{Fore.GREEN}Patients found!{Style.RESET_ALL}\n")
                print(hospital.searchPatients(id, string))
                sleep(0.3)
                system("cls||clear")
            elif option == '10':
                #indentify departaments which contain patients with a given first name
                system("cls||clear")
                firstName = input("First name: ")
                print(f"{Fore.GREEN}Departaments found!{Style.RESET_ALL}\n")
                print(hospital.filterDepsName(firstName))
                sleep(0.3)
                system("cls||clear")
            elif option == '11':
                #form groups of k patiens from the same departaments with the same disease(k is given)
                system("cls||clear")
                k = int(input("k: "))
                print(f"{Fore.GREEN}Groups formed successfully!{Style.RESET_ALL}\n")
                print(hospital.formKGroupsInEachDep(k))
                sleep(0.3)
                system("cls||clear")
            elif option == '12':
                #form groups of k departaments having at most p patients that suffer from the same disease(k and p are given)
                system("cls||clear")
                k = int(input("k: "))
                p = int(input("p: "))
                print(f"{Fore.GREEN}Groups formed successfully!{Style.RESET_ALL}\n")
                print(hospital.formKGroupsInEachDep(k, p))
                sleep(0.3)
                system("cls||clear")
            else:
                system("cls||clear")
                raise TypeError("Invalid option!")
    except ValueError as e:
        print(f"{Fore.RED}{e}{Style.RESET_ALL}")
        sleep(1)
        system("cls||clear")
    except TypeError as e:
        print(f"{Fore.RED}{e}{Style.RESET_ALL}")
        sleep(1)
        system("cls||clear")
    except Exception as e:
        print(f"{Fore.RED}{e}{Style.RESET_ALL}")
        sleep(1)
        system("cls||clear")


if __name__ == "__main__":
    print("This module is not meant to be run by itself!")
    from main import main
    main()