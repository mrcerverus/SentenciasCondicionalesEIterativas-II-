""" Importacion sys """
import sys
""" Dicc con ventas """
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}
""" ingreso de valor a filtrar """
valor = float(sys.argv[1])
# ("Ingrese umbral para el reporte: \n")
resultado = dict()
""" Filtrado por formula """
for (mes,value) in ventas.items():
    if value >= valor:
        resultado[mes] = value
print(resultado)

""" Filtrado por filter lambda 
newDict = []
newDict = dict(filter(lambda elem: elem[1] >= valor, ventas.items()))
print(newDict)
"""