"""
Programa: Calculadora de área de un rectángulo
Descripción: Este programa solicita al usuario la base y la altura de un rectángulo,
calcula el área y muestra el resultado. Se utilizan diferentes tipos de datos: float,
integer, string y boolean. El código sigue las convenciones de nomenclatura (snake_case) en Python.
"""
# Función que calcula el área del rectángulo
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área del rectángulo dados base y altura."""
    return base * altura

# Mensaje de bienvenida
print("Bienvenido al programa para calcular el área de un rectángulo.")

# Solicita los datos al usuario
base_ingresada = input("Ingresa la base del rectángulo (en cm): ")
altura_ingresada = input("Ingresa la altura del rectángulo (en cm): ")

# Conversión de datos de entrada (string) a float
base = float(base_ingresada)
altura = float(altura_ingresada)

# Validación booleana
es_valido = base > 0 and altura > 0

# Mostrar resultados
if es_valido:
    area = calcular_area_rectangulo(base, altura)
    print(f"\nEl área del rectángulo es: {area} cm²")
else:
    print("\nError: La base y la altura deben ser números positivos.")
