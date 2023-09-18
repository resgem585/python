def get_packages_info(packages):
    #"Crea un diccionario para almacenar la información de los paquetes"
    packages_info = {
        "total_weight": 0,     # "Inicializa el peso total en 0"
        "destinations": {}     # "Inicializa el diccionario de destinos vacío
    }
    
    # "Itera sobre cada paquete en la lista de paquetes"
    for package in packages:
        if package[2] in packages_info["destinations"]:
            # "Si el destino ya está en el diccionario de destinos, incrementa su contador en 1"
            packages_info["destinations"][package[2]] += 1
        else:
            # "Si el destino no está en el diccionario de destinos, crea una nueva entrada y establece su contador en 1"
            packages_info["destinations"][package[2]] = 1
        
        # "Suma el peso del paquete al peso total"
        packages_info["total_weight"] += package[1]
    

    # "Redondea el peso total a 2 decimales"
    packages_info["total_weight"] = round(packages_info["total_weight"], 2)
    
    # "Devuelve el diccionario con la información de los paquetes"
    return packages_info


get_packages_info([
    (1, 20, "Mexico"),
    (2, 15.5, "Colombia"),
    (3, 30, "Mexico"),
    (4, 12, "Argentina"),
    (5, 8.2, "Colombia"),
    (6, 25, "Mexico"),
    (7, 18.7, "Argentina"),
    (8, 5, "Colombia"),
    (9, 22.3, "Argentina"),
    (10, 14.8, "Colombia")
])
