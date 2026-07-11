Frutas = ["Banano", "Fresa", "Manzana", "Sandia","Pera"]
print(Frutas[0])

Frutas.append("Uva")
print(Frutas[5])

Frutas[2]="Naranja"
print(Frutas[2])

print("------------")
for Fruta in Frutas:
    print(Fruta)

print("------------------")

DicFruta={"Nombre":"Naranja", "Color":"Amarillo", "Tamaño":"Grande", "Sabor":"Dulce"}
print(DicFruta["Nombre"])
print(DicFruta["Tamaño"])
print(DicFruta.get("Tamano"))

print("----------------")

for clave, valor in DicFruta.items():
    print(clave, valor)

print("---------------")

Dic1 = {"Fecha":"10/07/2026", "Tipo":"Electrónico", "Monto":93500}
Transacciones = [{"Fecha":"10/07/2026", "Tipo":"Electrónico", "Monto":-93500}, 
                 {"Fecha":"04/07/2026", "Tipo": "Físico", "Monto":130000},
                 {"Fecha":"01/01/2026", "Tipo":"Físico", "Monto":-66000},
                 {"Fecha":"03/07/2026", "Tipo": "Electrónico", "Monto":-1250000},
                 {"Fecha":"06/07/2026", "Tipo":"Electrónico", "Monto":193000}]

print(Transacciones[2]["Monto"])
Total=0

for t in Transacciones:
    print(t)
    print("-------------")
    Total += t["Monto"]

print(Total)
print("-----------------------------")

Total2 = sum(t["Monto"] for t in Transacciones)
print("Este es el segundo total", Total2)

Retiros = [t for t in Transacciones if t["Monto"] < 0]
print(Retiros)
