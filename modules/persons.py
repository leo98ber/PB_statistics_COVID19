from os import error
from modules import donwload,errors,read,delete
from time import sleep,time

class Person(object):
    
    def __init__(self,handler,info_person,driver):
        self.driver = driver
        self.handler = handler
        self.info_person = info_person
        self.info_person.exist()
        self.persons = self.handler.reader()

    @errors.value_error
    @errors.error_decorate
    @errors.type_error
    def create(self):
        cedula,nombre,estado,municipio,parroquia = donwload.donwload_person(self.driver)
        confirm = input("\n\nDesea guardar los datos de este ciudadano?(y/n): ").lower()

        if confirm == "y":
            exist = read.exist(self.persons,cedula)

            if exist == 0:
                self.handler.creater(cedula,nombre,estado,municipio,parroquia)
                print("Se ha guardado su busqueda")
            else:
                print("No se pudo crear el cliente debido a que este ya existe en la base de datos local")

            
        elif confirm == "n":
            print("No se ha guarado la busqueda")
            
        else: 
            print("Opcion invalida,No se ha guarado la busqueda")


    @errors.tag_doesnt_exist
    @errors.client_doesnt_exist
    def read(self):
        option = input("\nIndique que desea visualizar:\n").lower().strip()

        if option == "list_persons":
            print("\nLista de ciudadanos\n")
            for person in self.persons:
                print("\n",person)

        elif option == "filter_persons":
            tag = input("\nIntroduzca un tag para filtrar: \n").lower().strip()
            keyword = input("\nIntroduzca informacion clave para la busqueda\n").lower().strip()
            read.filter(self.persons,keyword,tag)

        elif option == "person":
            pk = input("\nIndique la cedula del ciudadano que desea visualizar: \n").upper().strip() 
            print(pk)
            read.search(self.persons,pk)

        else:
            print("\nError usted introdujo una opcion invalida intente de nuevo\n")




    @errors.client_doesnt_exist
    def delete(self): 
        pk = input("\nIndique la cedula del ciudadano que desea eliminar de la base de datos local\n").upper().strip() 
        delete.delete(self.handler,self.persons,pk)