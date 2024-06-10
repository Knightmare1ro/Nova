Productos = [["Huevo", "Papas", "Tomate"],
             [30, 12, 8],
             [1.00, 3.00, 4.00],
]
print(Productos)

Gestionar = int(input("Que se desea hacer? (1)Agregar, (2)Eliminar, (3)Actualizar, (4)Visualizar: "))
if Gestionar == 1:
    Productos.append()
    print(Productos)

elif Gestionar ==2:
    Productos.remove()
    print(Productos)

elif Gestionar == 3:
    Productos.insert()

elif Gestionar == 4:
    print(Productos)
