# Proyecto: [Modulos Y Funciones de Python]
# Estudiante: [Felipe Mata]
# Fecha de Inicio: [22/8/2025]
# Fecha de Entrega: []
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.


#from analisis_datos.carga_datos import generar_lista_compras
#from analisis_datos.estadisticas import media

from analisis_datos import *

def saludar():
    print("Hola desde la funcion")
    
if __name__ == "__main__":
    compras = generar_lista_compras()
    print(compras)
    media = media(list(compras.values()))
    mediana = mediana(list(compras.values()))
    
    print("Mediana de costo por articulo: " , mediana)
    print("Promedio de costo por articulo: " , media)

