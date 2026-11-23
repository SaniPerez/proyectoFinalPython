import operaciones
from base_datos import crear_tabla

# Creacion de la tabla SQL
crear_tabla()

while True:
    print("Sistema de gestion de productos".upper())
    print("1. Registrar producto")
    print("2. Visualizar producto")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Reporte de productos (cantidad <= a límite ingresado)")
    print("7. Salir")
    
    opcion = input("Seleccionar una opcion: ").strip()
    
    match opcion:
        # Dar de alta producto
        case "1":   
            operaciones.agregar_productos()        
        
        # Visualizar productos
        case "2":
            operaciones.mostrar_todos_los_productos()
            
        # Buscar de producto por ID
        case "3":
            operaciones.buscar_productos_por_id()
            
        # Actualizar producto
        case "4":
            operaciones.actualizar_producto_por_id()
        
        # Eliminar producto
        case "5":
            operaciones.eliminar_productos()  
              
        # Reporte de stock minimo 
        case "6":
            operaciones.reporte_stock_minimo()
               
        # Salir del programa  
        case "7":
            print("Usted está saliendo del programa...")
            break
            
        case _:
            print("La opción que ingresó es incorrecta, vuelva a intentarlo")
            continue
