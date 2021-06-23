import os


def create_or_open_file(path, file):
	'''if the file does not exist, it creates it'''
    folder_path = os.path.join(path, file)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    return folder_path


path = os.path.dirname(os.path.abspath(__file__))
file = "agenda.txt"
agenda = create_or_open_file(path, file)


def write_on_file(agenda, name, id, cel):
	'''Add record at file'''
    with open(agenda, 'a') as file:
        file.write(name + '\n') 
        file.write(id + '\n') 
        file.write(cel + '\n')
        file.close()
    return print(
        f'Se ingresaron los datos nombre:\
            {name}, cedula: {id} y celular: {cel}')


def look_at_file(name):
	'''look a record by name'''
    with open(agenda, 'a') as file:
        for names, id, cel in agenda:
            if names == name:
                file.close()
                return (name, id, cel)


def look_cel_at_file(name):
	'''Look a record at file by name and return cel'''
    with open(agenda, 'r') as file:
        registros = file.readlines()
        register_name = str(name + '\n')
        for i, names in enumerate(registros):
            if names == register_name:
                file.close()
                return registros[i+2]
            i += i
        return "Los valores no se encontraron"


def look_name_and_cel_at_file(id):
    with open(agenda, 'r') as file:
        registros = file.readlines()
        register_id = str(id + '\n')
        for i, id in enumerate(registros):
            if id == register_id:
                file.close()
                return (registros[i-1], registros[i+1])
            i += i
        return "Los valores no se encontraron"


def delete_record_at_file(name, id, cel):
	'''Delete a record at file'''
    with open(agenda, 'r',) as records:
        list_of_records = records.readlines()
    register_id = str(id + '\n')
    with open(agenda, "w") as records:
        for i in list_of_records:
            i = str(i)
            if (i != name) and (i != register_id) and (i != cel):
                records.write(i)
        records.close()
        return True


def print_list(agenda):
    with open(agenda, 'r',) as records:
        list_of_records = records.readlines()
    for i in list_of_records:
        print(i)
    return True


action = ""

while action != 6:
    print("Digite alguna de las siguientes opciones:")
    print("1. Ingresar nuevo registro")
    print("2. Buscar el celular")
    print("3. Mostrar todos los Registros")
    print("4. Mostrar Registros que empiecen por una letra")
    print("5. Eliminar Registro")
    print("6. Finalizar")

    action = int(input("Digite alguna de las opciones:"))
    if action == 1:
        name = input(print("Ingrese nombre y apellido: "))
        id = input(print("Ingrese numero de cedula: "))
        cel = input(print("Ingrese numero de celular: "))
        registros = open(agenda, "r")
        registros = registros.readlines()
        id_str = str(id + '\n')
        if id_str not in registros:
            write_on_file(agenda, name, id, cel)
        print(f"Esta cedula: {id} ya se encuentra en los registros")

    if action == 2:
        name = input(print("Ingrese nombre y apellido: "))
        cel = look_cel_at_file(name)
        print(f"Numero celular: {cel} del registro {name} ")

    if action == 3:
        recoders = print_list(agenda)
    if action == 4:
        search_for_letter = input("ingrese la letra por la cual desea buscar")
        registros = [
            print(x for x in agenda if x.startwith(search_for_letter))]
    if action == 5:
        id = input(
            "ingrese el numero de cedula del registro que desea eliminar")
        recoders = look_name_and_cel_at_file(id)
        name = recoders[0]
        print(name)
        cel = recoders[1]
        print(cel)
        delete = delete_record_at_fileat_file(name, id, cel)
        if delete:
            print(f'se borraron los datos : {name,id,cel}')
        else:
            print('no hay datos para borrar')
