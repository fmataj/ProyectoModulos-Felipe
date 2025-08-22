# estadisticas.py
def media(datos):
    media = sum(datos) / len(datos)
    return media


def mediana(datos):
    #primer paso ordenar datos
    datos = sorted(datos)
    n = len(datos)
    mitad = n // 2
    
    if n % 2 == 0:
        mediana ((datos[mitad -1] + datos[mitad])/2 )
    else:
        mediana = datos[mitad]
    return mediana



if __name__ == "__main__":
    notas = [100, 50,100,78,100]
    print(mediana(notas))