def cargarDatos():
    archivo = open("numeros.csv","r")
    lineas = archivo.readlines()
    print(lineas)
    datos = [0]*len(lineas)
    for linea in lineas:
        elemento = linea.split(",")
        datos.append(elemento)
    print(datos)
    with open("numeros1.txt","w") as archivo:
        for elemento in datos:
            str(elemento).split(",")
            for i in range(0,len(elemento)):
                archivo.write(elemento[i])



cargarDatos()