# Escribe un programa que defina las constantes IVA_GENERAL (0.21) e IVA_REDUCIDO
# (0.10) y las variables de un producto (nombre, base imponible). 
# Debe mostrar el precio final con cada uno de los dos tipos impositivos.

IVA_GENERAL = 0.21
IVA_REDUCIDO = 0.10

def main():
    nombre = input("Nombre del producto:" )
    precio = float(input("Precio del producto:"))
    pregunta_descuento = bool(input("Es con descuento o sin descuento? (true o false / 0 o 1):"))
    if pregunta_descuento == 1 or pregunta_descuento == true:
        precio_total = precio + (precio * IVA_REDUCIDO)
        print(f"{nombre}, valor de: {precio_total:.2f}")
    else:
        precio_total = precio + (precio * IVA_GENERAL)
        print(f"{nombre}, valor de: {precio_total:.2f}")

if __name__ == "__main__":
    main()