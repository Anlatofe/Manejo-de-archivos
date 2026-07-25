Archivo = "Palabras.txt"

def Adicionar():
    NuevasPalabras = ["Draw", "Sleep", "Sing", "Write", "Work"]
    with open(Archivo, "a") as File:
        for Palabra in NuevasPalabras:
            File.write(Palabra + "\n")


def ObtenerLetra():
    while True:
        Letra = input("Digite una letra ").upper().strip()
        if len(Letra) != 1:
            print("Por favor introduzca solo un caracter.")
        elif not Letra.isalpha():
            print("Debe ser un caracter alfabético.")
        else:
            return(Letra)
        

def Jugar():
    # Seleccionar Palabra al azar
    