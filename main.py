# Solución propuesta.

def es_cadena_valida(gramatica, cadena):
    longitud_cadena = len(cadena)
    if longitud_cadena == 0:
        return False

    # Crear tabla de sets
    tabla_cyk = [[set() for _ in range(longitud_cadena)] for _ in range(longitud_cadena)]

    # Rellenar la diagonal
    for i in range(longitud_cadena):
        terminal = cadena[i]
        for no_terminal, producciones in gramatica.items():
            for produccion in producciones:
                if len(produccion) == 1 and produccion[0] == terminal:
                    tabla_cyk[i][i].add(no_terminal)

    # Rellenar el resto de la tabla
    for longitud in range(2, longitud_cadena + 1):
        for inicio in range(longitud_cadena - longitud + 1):
            fin = inicio + longitud - 1
            for division in range(inicio, fin):
                lado_izquierdo = tabla_cyk[inicio][division]
                lado_derecho = tabla_cyk[division + 1][fin]

                for no_terminal, producciones in gramatica.items():
                    for produccion in producciones:
                        if len(produccion) == 2 and produccion[0] in lado_izquierdo and produccion[1] in lado_derecho:
                            tabla_cyk[inicio][fin].add(no_terminal)

    # Comprobar si la cadena es generada por la gramática
    return 'S' in tabla_cyk[0][longitud_cadena - 1]

def main():
    try:
        with open("Input.txt", "r") as archivo_entrada:
            num_casos = int(archivo_entrada.readline().strip())

            for _ in range(num_casos):
                primera_linea = archivo_entrada.readline().strip().split()
                num_no_terminales = int(primera_linea[0])
                num_cadenas = int(primera_linea[1])

                # Leer la gramática
                gramatica = {}
                for _ in range(num_no_terminales):
                    produccion = archivo_entrada.readline().strip().split()
                    no_terminal = produccion[0]
                    derivaciones = [list(derivacion) for derivacion in produccion[1:]]
                    gramatica[no_terminal] = derivaciones

                # Leer y procesar las cadenas
                for _ in range(num_cadenas):
                    cadena = archivo_entrada.readline().strip()
                    if es_cadena_valida(gramatica, cadena):
                        print("yes")
                    else:
                        print("no")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
