from DepartamentClass import Departament
from PatientClass import Patient
from Hospital import Hospital
from colorama import Fore, Back, Style
from SortingFuncs import srt, flt, srch
from os import system
from time import sleep

#le scriu pe tren doamne fereste sa le fac acum
def testAddDepartament():
    print(f"{Fore.BLUE}Testing AddDepartament...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    assert repository.departaments[0].id == 1, 'Departament id not added correctly!(1)'
    assert repository.departaments[0].name == 'Cardiology', 'Departament name not added correctly!(1)'
    assert repository.departaments[0].numberOfBeds == 20, 'Departament number of patients not added correctly!(1)'
    print(f"{Fore.GREEN}AddDepartament_1 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    assert repository.departaments[1].id == 2, 'Departament id not added correctly!(2)'
    assert repository.departaments[1].name == 'Neurology', 'Departament name not added correctly!(2)'
    assert repository.departaments[1].numberOfBeds == 15, 'Departament number of patients not added correctly!(2)'
    print(f"{Fore.GREEN}AddDepartament_2 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    dep = Departament(3, 'Oncology', 10)
    repository.departaments.append(dep)
    assert repository.departaments[2].id == 3, 'Departament id not added correctly!(3)'
    assert repository.departaments[2].name == 'Oncology', 'Departament name not added correctly!(3)'
    assert repository.departaments[2].numberOfBeds == 10, 'Departament number of patients not added correctly!(3)'
    print(f"{Fore.GREEN}AddDepartament_3 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    print(f"{Fore.LIGHTGREEN_EX}AddDepartament tested successfully!{Style.RESET_ALL}")
    sleep(0.02)

def testAddPatient():
    print(f"{Fore.BLUE}Testing AddPatient...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    patient = Patient('John', 'Doe', '1960115123456', 'heart disease')
    repository.departaments[0].patients.append(patient)
    assert repository.departaments[0].patients[0].firstName == 'John', 'Patient first name not added correctly!'
    assert repository.departaments[0].patients[0].lastName == 'Doe', 'Patient last name not added correctly!'
    assert repository.departaments[0].patients[0].code == '1960115123456', 'Patient code not added correctly!'
    assert repository.departaments[0].patients[0].disease == 'heart disease', 'Patient disease not added correctly!'
    print(f"{Fore.GREEN}AddPatient_1 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    patient = Patient('Jane', 'Doe', '1960115123457', 'heart disease')
    repository.departaments[0].patients.append(patient)
    assert repository.departaments[0].patients[1].firstName == 'Jane', 'Patient first name not added correctly!'
    assert repository.departaments[0].patients[1].lastName == 'Doe', 'Patient last name not added correctly!'
    assert repository.departaments[0].patients[1].code == '1960115123457', 'Patient code not added correctly!'
    assert repository.departaments[0].patients[1].disease == 'heart disease', 'Patient disease not added correctly!'
    print(f"{Fore.GREEN}AddPatient_2 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    patient = Patient('Maleu', 'Testere', '1960015123458', 'heart disease')
    repository.departaments[0].patients.append(patient)
    assert repository.departaments[0].patients[2].firstName == 'Maleu', 'Patient first name not added correctly!'
    assert repository.departaments[0].patients[2].lastName == 'Testere', 'Patient last name not added correctly!'
    assert repository.departaments[0].patients[2].code == '1960015123458', 'Patient code not added correctly!'
    assert repository.departaments[0].patients[2].disease == 'heart disease', 'Patient disease not added correctly!'
    print(f"{Fore.GREEN}AddPatient_3 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    print(f"{Fore.LIGHTGREEN_EX}AddPatient tested successfully!{Style.RESET_ALL}")
    sleep(0.02)

def testRemovePatient():
    print(f"{Fore.BLUE}Testing RemovePatient...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    patient = Patient('John', 'Doe', '1960115123456', 'heart disease')
    repository.departaments[0].patients.append(patient)
    patient = Patient('Jane', 'Doe', '1960115123457', 'heart disease')
    repository.departaments[0].patients.append(patient)
    patient = Patient('Maleu', 'Testere', '1960015123458', 'heart disease')
    repository.departaments[0].patients.append(patient)
    repository.removePatient(0, '1960115123456')
    assert len(repository.departaments[0].patients) == 2, 'Patient not removed correctly! (1)'
    assert repository.departaments[0].patients[0].firstName == 'Jane', 'Patient not removed correctly! (1)'
    print(f"{Fore.GREEN}RemovePatient_1 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    repository.removePatient(0, '1960115123457')
    assert len(repository.departaments[0].patients) == 1, 'Patient not removed correctly! (2)'
    assert repository.departaments[0].patients[0].firstName == 'Maleu', 'Patient not removed correctly! (2)'
    print (f"{Fore.GREEN}RemovePatient_2 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    repository.removePatient(0, '1960015123458')
    assert len(repository.departaments[0].patients) == 0, 'Patient not removed correctly! (3)'
    print(f"{Fore.GREEN}RemovePatient_3 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    print(f"{Fore.LIGHTGREEN_EX}RemovePatient tested successfully!{Style.RESET_ALL}")
    sleep(0.02)

def testRemoveDepartament():
    print(f"{Fore.BLUE}Testing RemoveDepartament...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    dep = Departament(3, 'Oncology', 10)
    repository.departaments.append(dep)
    repository.removeDepartament(1)
    print (len(repository.departaments))
    assert len(repository.departaments) == 2, 'Departament not removed correctly! (1)'
    assert repository.departaments[0].name == 'Neurology', 'Departament not removed correctly! (1)'
    print(f"{Fore.GREEN}RemoveDepartament_1 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    repository.removeDepartament(2)
    assert len(repository.departaments) == 1, 'Departament not removed correctly! (2)'
    assert repository.departaments[0].name == 'Oncology', 'Departament not removed correctly! (2)'
    print(f"{Fore.GREEN}RemoveDepartament_2 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    repository.removeDepartament(3)
    assert len(repository.departaments) == 0, 'Departament not removed correctly! (3)'
    print(f"{Fore.GREEN}RemoveDepartament_3 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    print(f"{Fore.LIGHTGREEN_EX}RemoveDepartament tested successfully!{Style.RESET_ALL}")
    sleep(0.02)

def testSortDepsNOP():
    print(f"{Fore.BLUE}Testing SortDepsNOP...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    dep = Departament(3, 'Oncology', 10)
    repository.departaments.append(dep)
    repository.departaments[0].patients.append(Patient('John', 'Doe', '1960115123456', 'heart disease'))
    repository.departaments[0].patients.append(Patient('Jane', 'Doe', '1960115123457', 'heart disease'))
    repository.departaments[1].patients.append(Patient('Maleu', 'Testere', '1960015123458', 'heart disease'))
    repository.departaments[1].patients.append(Patient('John', 'Doe', '1960115123459', 'heart disease'))
    repository.departaments[1].patients.append(Patient('Jane', 'Doe', '1960115123450', 'heart disease'))
    repository.departaments[2].patients.append(Patient('Maleu', 'Testere', '1960015123451', 'heart disease'))
    repository.sortDepsNOP()
    assert repository.departaments[0].name == 'Neurology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[1].name == 'Cardiology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[2].name == 'Oncology', 'Departaments not sorted correctly!(1)'
    print(f"{Fore.GREEN}SortDepsNOP_1 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    repository.departaments[0].patients.append(Patient('John', 'Doe', '1960115123452', 'heart disease'))
    repository.sortDepsNOP()
    assert repository.departaments[0].name == 'Neurology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[1].name == 'Cardiology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[2].name == 'Oncology', 'Departaments not sorted correctly!(1)'
    print(f"{Fore.GREEN}SortDepsNOP_2 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    repository.departaments[2].patients.append(Patient('John', 'Doe', '1960115123453', 'heart disease'))
    repository.departaments[2].patients.append(Patient('John', 'Doe', '1960115123454', 'heart disease'))
    repository.departaments[2].patients.append(Patient('John', 'Doe', '1960115123455', 'heart disease'))
    repository.sortDepsNOP()
    assert repository.departaments[0].name == 'Neurology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[1].name == 'Oncology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[2].name == 'Cardiology', 'Departaments not sorted correctly!(1)'
    print(f"{Fore.GREEN}SortDepsNOP_3 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    print(f"{Fore.LIGHTGREEN_EX}SortDepsNOP tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
def testSortDepsAge():
    pass
    print(f"{Fore.BLUE}Testing SortDepsAge...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    repository.departaments[0].patients.append(Patient('test', 'testescu', '1960000000000', 'test'))
    repository.departaments[0].patients.append(Patient('test', 'testescu', '1970000000000', 'test'))
    repository.departaments[0].patients.append(Patient('test', 'testescu', '1980000000000', 'test'))
    repository.departaments[0].patients.append(Patient('test', 'testescu', '1990000000000', 'test'))
    repository.departaments[1].patients.append(Patient('test', 'testescu', '5000000000000', 'test'))
    repository.departaments[1].patients.append(Patient('test', 'testescu', '5010000000000', 'test'))
    repository.departaments[1].patients.append(Patient('test', 'testescu', '5020000000000', 'test'))
    repository.departaments[1].patients.append(Patient('test', 'testescu', '5030000000000', 'test'))
    repository.departaments[1].patients.append(Patient('test', 'testescu', '5040000000000', 'test'))
    repository.sortDepsAge(25)
    assert repository.departaments[0].name == 'Cardiology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[1].name == 'Neurology', 'Departaments not sorted correctly!(1)'
    print(f"{Fore.GREEN}SortDepsAge_1 tested successfully!{Style.RESET_ALL}")
    repository.departaments.clear()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    repository.departaments[1].patients.append(Patient('test', 'testescu', '1960000000000', 'test'))
    repository.departaments[1].patients.append(Patient('test', 'testescu', '1970000000000', 'test'))
    repository.departaments[1].patients.append(Patient('test', 'testescu', '1980000000000', 'test'))
    repository.departaments[1].patients.append(Patient('test', 'testescu', '1990000000000', 'test'))
    repository.departaments[0].patients.append(Patient('test', 'testescu', '5000000000000', 'test'))
    repository.departaments[0].patients.append(Patient('test', 'testescu', '5010000000000', 'test'))
    repository.departaments[0].patients.append(Patient('test', 'testescu', '5020000000000', 'test'))
    repository.departaments[0].patients.append(Patient('test', 'testescu', '5030000000000', 'test'))
    repository.departaments[0].patients.append(Patient('test', 'testescu', '5040000000000', 'test'))
    repository.sortDepsAge(24)
    print(repository)
    assert repository.departaments[0].name == 'Neurology', 'Departaments not sorted correctly!(2)'
    assert repository.departaments[1].name == 'Cardiology', 'Departaments not sorted correctly!(2)'
    print(f"{Fore.GREEN}SortDepsAge_2 tested successfully!{Style.RESET_ALL}")
    print(f"{Fore.LIGHTGREEN_EX}SortDepsAge tested successfully!{Style.RESET_ALL}")
    sleep(0.02)

def testSortuVietiiMele():
    print(f"{Fore.BLUE}Testing SortuVietiiMele...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    dep = Departament(3, 'Oncology', 10)
    repository.departaments.append(dep)
    repository.departaments[0].patients.append(Patient('1', 'a', '1960000000000', 'test'))    
    repository.departaments[0].patients.append(Patient('2', 'b', '5080000000000', 'test'))
    repository.departaments[0].patients.append(Patient('3', 'c', '1560000000000', 'test'))
    repository.departaments[1].patients.append(Patient('4', 'd', '4030000000000', 'test'))
    repository.departaments[1].patients.append(Patient('5', 'e', '1960000000000', 'test'))
    repository.departaments[2].patients.append(Patient('6', 'f', '1990000000000', 'test'))
    repository.departaments[2].patients.append(Patient('7', 'g', '1300000000000', 'test'))
    repository.departaments[2].patients.append(Patient('8', 'h', '1930000000000', 'test'))
    repository.departaments[2].patients.append(Patient('9', 'i', '1900000000000', 'test'))
    repository.sortuVietiiMele()
    assert repository.departaments[0].name == 'Oncology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[1].name == 'Cardiology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[2].name == 'Neurology', 'Departaments not sorted correctly!(1)'
    assert repository.departaments[0].patients[0].firstName == '6', 'Patients not sorted correctly!(1)'
    assert repository.departaments[0].patients[1].firstName == '7', 'Patients not sorted correctly!(1)'
    assert repository.departaments[0].patients[2].firstName == '8', 'Patients not sorted correctly!(1)'
    assert repository.departaments[0].patients[3].firstName == '9', 'Patients not sorted correctly!(1)'
    assert repository.departaments[1].patients[0].firstName == '1', 'Patients not sorted correctly!(1)'
    assert repository.departaments[1].patients[1].firstName == '2', 'Patients not sorted correctly!(1)'
    assert repository.departaments[1].patients[2].firstName == '3', 'Patients not sorted correctly!(1)'
    assert repository.departaments[2].patients[0].firstName == '4', 'Patients not sorted correctly!(1)'
    assert repository.departaments[2].patients[1].firstName == '5', 'Patients not sorted correctly!(1)'
    print(f"{Fore.GREEN}SortuVietiiMele_1 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    repository.departaments.clear()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    dep = Departament(3, 'Oncology', 10)
    repository.departaments.append(dep)
    repository.departaments[0].patients.append(Patient('2', 'b', '1960000000000', 'test'))    
    repository.departaments[0].patients.append(Patient('1', 'a', '5080000000000', 'test'))
    repository.departaments[0].patients.append(Patient('3', 'c', '1560000000000', 'test'))
    repository.departaments[1].patients.append(Patient('5', 'e', '4030000000000', 'test'))
    repository.departaments[1].patients.append(Patient('4', 'd', '1960000000000', 'test'))
    repository.departaments[2].patients.append(Patient('7', 'g', '1990000000000', 'test'))
    repository.departaments[2].patients.append(Patient('9', 'i', '1300000000000', 'test'))
    repository.departaments[2].patients.append(Patient('6', 'f', '1930000000000', 'test'))
    repository.departaments[2].patients.append(Patient('8', 'h', '1900000000000', 'test'))
    repository.sortuVietiiMele()
    assert repository.departaments[0].patients[0].firstName == '6', 'Patients not sorted correctly!(1)'
    assert repository.departaments[0].patients[1].firstName == '7', 'Patients not sorted correctly!(1)'
    assert repository.departaments[0].patients[2].firstName == '8', 'Patients not sorted correctly!(1)'
    assert repository.departaments[0].patients[3].firstName == '9', 'Patients not sorted correctly!(1)'
    assert repository.departaments[1].patients[0].firstName == '1', 'Patients not sorted correctly!(1)'
    assert repository.departaments[1].patients[1].firstName == '2', 'Patients not sorted correctly!(1)'
    assert repository.departaments[1].patients[2].firstName == '3', 'Patients not sorted correctly!(1)'
    assert repository.departaments[2].patients[0].firstName == '4', 'Patients not sorted correctly!(1)'
    assert repository.departaments[2].patients[1].firstName == '5', 'Patients not sorted correctly!(1)'
    print(f"{Fore.GREEN}SortuVietiiMele_2 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    print(f"{Fore.LIGHTGREEN_EX}SortuVietiiMele tested successfully!{Style.RESET_ALL}")
    sleep(0.02)

def testFilterDepsAge():
    print(f"{Fore.BLUE}Testing FilterDepsAge...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    dep = Departament(3, 'Oncology', 10)
    repository.departaments.append(dep)
    repository.departaments[0].patients.append(Patient('John', 'Doe', '1960000000000', 'test'))
    repository.departaments[0].patients.append(Patient('Jane', 'Doe', '5020000000000', 'test'))
    repository.departaments[1].patients.append(Patient('Maleu', 'Test', '1960000000000', 'test'))
    repository.departaments[1].patients.append(Patient('John', 'Doe', '5030000000000', 'test'))
    repository.departaments[2].patients.append(Patient('Jane', 'Doe', '1560000000000', 'test'))
    repository.filterDepsAge(60)
    assert repository.departaments[0].name == 'Cardiology', 'Departaments not filtered correctly!(1)'
    assert repository.departaments[1].name == 'Neurology', 'Departaments not filtered correctly!(1)'
    assert repository.departaments[2].name == 'Oncology', 'Departaments not filtered correctly!(1)'
    print(f"{Fore.GREEN}FilterDepsAge_1 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    repository.departaments[0].patients.append(Patient('John', 'Doe', '1960000000000', 'test'))
    repository.departaments[2].patients.append(Patient('Jane', 'Doe', '1560000000000', 'test'))
    repository.filterDepsAge(50)
    assert repository.departaments[0].name == 'Cardiology', 'Departaments not filtered correctly!(2)'
    assert repository.departaments[1].name == 'Neurology', 'Departaments not filtered correctly!(2)'
    assert repository.departaments[2].name == 'Oncology', 'Departaments not filtered correctly!(2)'
    print(f"{Fore.GREEN}FilterDepsAge_2 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    repository.departaments[0].patients.append(Patient('John', 'Doe', '1960000000000', 'test'))
    repository.departaments[2].patients.append(Patient('Jane', 'Doe', '1560000000000', 'test'))
    repository.filterDepsAge(15)
    assert repository.departaments[0].name == 'Cardiology', 'Departaments not filtered correctly!(3)'
    assert repository.departaments[1].name == 'Neurology', 'Departaments not filtered correctly!(3)'
    assert repository.departaments[2].name == 'Oncology', 'Departaments not filtered correctly!(3)'
    print(f"{Fore.GREEN}FilterDepsAge_3 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    print(f"{Fore.LIGHTGREEN_EX}FilterDepsAge tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    
def testSearchPatients():
    print(f"{Fore.BLUE}Testing SearchPatients...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    patient = Patient('John', 'Doe', '1960115123456', 'heart disease')
    repository.departaments[0].patients.append(patient)
    patient = Patient('Maricel', 'Doe', '1960115123457', 'heart disease')
    repository.departaments[0].patients.append(patient)
    patient = Patient('Maleu', 'Testere', '1960015123458', 'heart disease')
    repository.departaments[0].patients.append(patient)
    assert repository.searchPatients(0, 'John') == [repository.departaments[0].patients[0]], 'Patients not searched correctly!(1)'
    print(f"{Fore.GREEN}SearchPatients_1 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    assert repository.searchPatients(0, 'Maricel') == [repository.departaments[0].patients[1]], 'Patients not searched correctly!(2)'
    print(f"{Fore.GREEN}SearchPatients_2 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    assert repository.searchPatients(0, 'tere') == [repository.departaments[0].patients[2]], 'Patients not searched correctly!(3)'
    print(f"{Fore.GREEN}SearchPatients_3 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    print(f"{Fore.LIGHTGREEN_EX}SearchPatients tested successfully!{Style.RESET_ALL}")
    sleep(0.02)

def testFilterDepsName():
    print(f"{Fore.BLUE}Testing FilterDepsName...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    patient = Patient('John', 'Doe', '1960115123456', 'heart disease')
    repository.departaments[0].patients.append(patient)
    patient = Patient('Maricel', 'Doe', '1960115123457', 'heart disease')
    repository.departaments[0].patients.append(patient)
    patient = Patient('Maleu', 'Testere', '1960015123458', 'heart disease')
    repository.departaments[0].patients.append(patient)
    assert repository.filterDepsName('John') == [repository.departaments[0]], 'Departaments not filtered correctly!(1)'
    print(f"{Fore.GREEN}FilterDepsName_1 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    assert repository.filterDepsName('Maricel') == [repository.departaments[0]], 'Departaments not filtered correctly!(2)'
    print(f"{Fore.GREEN}FilterDepsName_2 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    assert repository.filterDepsName('tere') == [], 'Departaments not filtered correctly!(3)'
    print(f"{Fore.GREEN}FilterDepsName_3 tested successfully!{Style.RESET_ALL}")
    sleep(0.02)
    print(f"{Fore.LIGHTGREEN_EX}FilterDepsName tested successfully!{Style.RESET_ALL}")
    sleep(0.02)

def testFormKGroupsInEachDep():
    #bafta charlie
    pass
    print(f"{Fore.BLUE}Testing FormKGroupsInEachDep...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    dep = Departament(3, 'Oncology', 10)
    repository.departaments.append(dep)

def testFormKGroupsInEachDepCuP():
    #bafta charlie v2.0
    pass
    print(f"{Fore.BLUE}Testing FormKGroupsInEachDepCuP...{Style.RESET_ALL}")
    sleep(0.02)
    repository = Hospital()
    dep = Departament(1, 'Cardiology', 20)
    repository.departaments.append(dep)
    dep = Departament(2, 'Neurology', 15)
    repository.departaments.append(dep)
    dep = Departament(3, 'Oncology', 10)
    repository.departaments.append(dep)

def testAll():
    # try:    
    testAddDepartament()
    testAddPatient()
    testRemovePatient()
    testRemoveDepartament()
    testSortDepsNOP()
    testSortDepsAge()
    testSortuVietiiMele()
    testFilterDepsAge()
    testSearchPatients()
    testFilterDepsName()
    testFormKGroupsInEachDep()
    testFormKGroupsInEachDepCuP()
    # except AssertionError as ae:
    #     print(f"{Fore.RED}{ae}{Style.RESET_ALL}")
    #     sleep(0.02)
    #     print(f"{Back.RED}{Fore.LIGHTRED_EX}Tests failed!{Style.RESET_ALL}")
    #     sleep(0.02)
    #     return
    # except Exception as ex:
    #     print(f"{Fore.RED}{ex}{Style.RESET_ALL}")
    #     sleep(0.02)
    #     print(f"{Back.RED}{Fore.LIGHTRED_EX}Tests failed!{Style.RESET_ALL}")
    #     sleep(0.02)
    #     return
    print(f"{Fore.LIGHTGREEN_EX}Tests passed successfully!{Style.RESET_ALL}")
    sleep(2)
    system('cls||clear')
    
if __name__ == "__main__":
    testAll()
    sleep(0.02)
    input("Press Enter to continue...")