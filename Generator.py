from random import randint as rand
from random import choice as choice

def generator(repository, numberOfDepartaments = 15, numberOfPatients = 20):
    from DepartamentClass import Departament
    from PatientClass import Patient
    #dictionary for first names:
    firstName_dict:dict
    firstName_dict = {1:'Mihai', 2:'Alexandru', 3:'Marius', 4:'Geanina', 5:'Gabriel', 6:'Teodora(fara th)', 7:'Diana', 8:'Valentin', 9:'Dorian', 10:'Luis', 11:'Lucretia', 12:'Bogdan', 13:'Cristian', 14:'Cristina', 15:'Geani', 16:'Giddeon'}
    #dictionary for last names:
    lastName_dict = {1:'De la Suceava', 2:"Pescaru'", 3:'Popa', 4:'Vijelie', 5:'Stan', 6:'Visinoiu', 7:"Izotericu'", 8:'Mirabeliu', 9:'Hanu', 10:'Catanas', 11:'Serifu Thauu', 12:'Ghilencea', 13:'Vilcu', 14:"De La Sinaia", 15:"Milionaru'", 16:"Shefu'"}
    #dictionary for diseases:
    disease_dict = {1:'Cancer', 2:'Sifilis', 3:'Ebola', 4:'Covid-19', 5:'Utilizator Arch Linux', 6:'Manelist', 7:'Windows enjoyer', 8:'Boala Copiilor', 9:'Conducator BMW', 10:'Conducator Audi', 11:'Bombardier', 12:'Nu stie sa numere indexurile la dict',13:'Mort', 14:'Viu', 15:'Impiedicat', 16:'Analfabet'}
    #dictionary for departaments:
    departament_dict = {0:'Cardiologie', 1:'Neurologie', 2:"Efectiv Spitalu' 9", 3:'Pediatrie', 4:'Unixologie', 5:'Dermatologie', 6:'Chirurgie', 7:'Ortopedie', 8:'Audiologie', 9:'Nebunie', 10:'Oftalmologie', 11:'O.R.L.', 12:'Stomatologie', 13:'Endocrinologie', 14:'Diabet', 15:'Lift(s-a umplut spitalu punem unde putem)'}
    for i in range(numberOfDepartaments):
        repository.departaments.append(Departament(i+1, departament_dict[i], rand(17, 30)))
        for j in range(numberOfPatients):
            repository.departaments[i].patients.append(Patient(firstName_dict[rand(1, 16)], lastName_dict[rand(1, 16)], codeGen(), disease_dict[rand(1, 16)]))
        

#function for generating valid codes:
def codeGen():
    code = ''
    i = choice([1, 2, 6, 5])
    #1/13 digits
    code += str(i)
    #3/13 digits
    if i == 1 or i == 2:
        code +=str(rand(60, 99))
    else:
        var =str(rand(1, 23))
        if len(var) == 1:
            var = '0' + var
        code += var
    #5/13 digits
    var = str(rand(1, 12))
    if len(var) == 1:
        var = '0' + var
    code += var
    #7/13 digits
    if var == '02':
        var2 = str(rand(1, 28))
        if len(var2) == 1:
            var2 = '0' + var2
        code += var2
    elif var == '04' or var == '06' or var == '09' or var == '11':
        var2 = str(rand(1, 30))
        if len(var2) == 1:
            var2 = '0' + var2
        code += var2
    else:
        var2 = str(rand(1, 31))
        if len(var2) == 1:
            var2 = '0' + var2
        code += var2
    #9/13 digits
        var = str(rand(1, 52))
    if len(var) == 1:
        var = '0' + var
    code += var
    #12/13 digits
    var = str(rand(1, 999))
    if len(var) == 1:
        var = '00' + var
    elif len(var) == 2:
        var = '0' + var
    code += var
    #13/13 digits
    code += str(rand(0, 9))
    return code

if __name__ == "__main__":
    print("This module is not meant to be run by itself!")
    from main import main
    main()