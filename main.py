import json

def guardar_datos_usuario(nombre_archivo, datos):
    with open(nombre_archivo, "w") as f:
        json.dump(datos, f)
    print("Datos guardados correctamente")

def cargar_datos_usuario(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as f:
            datos = json.load(f)
        print("Datos cargados correctamente")
    except FileNotFoundError:
        print("No se encontró archivo de datos previo")
        return None

# Calcula el IMC usando peso y altura en metros
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Devuelve la categoría según el valor del IMC
def interpretar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Calcula la TMB (Tasa Metabólica Basal)
def calcular_tmb(peso, altura_cm, edad, genero):
    if genero == "hombre":
        return 88.362 + (13.397 * peso) + (4.799 * altura_cm) - (5.677 * edad)
    elif genero == "mujer":
        return 447.593 + (9.247 * peso) + (3.098 * altura_cm) - (4.330 * edad)
    else:
        raise ValueError("Género no válido. Por favor, introduce 'hombre' o 'mujer'.")

# Muestra los niveles de actividad física
def mostrar_niveles_actividad():
    print("\nSelecciona tu nivel de actividad física:")
    print("1. Sedentario (poco o ningún ejercicio)")
    print("2. Ligero (ejercicio ligero 1-3 días/semana)")
    print("3. Moderado (ejercicio moderado 3-5 días/semana)")
    print("4. Intenso (ejercicio intenso 6-7 días/semana)")
    print("5. Muy intenso (trabajo fisico duro o entrenamiento diario)")

# Calcula el factor de actividad según el nivel de actividad
def obtener_factor_actividad(opcion):
    factores = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }
    return factores.get(opcion, None)

# Solicita el nivel de actividad física con validación
def pedir_nivel_actividad():
    while True:
        try:
            opcion = int(input("Introduce el número de tu nivel de actividad (1-5): "))
            if opcion in range(1, 6):
                return opcion
            else:
                print("Número fuera de rango. Por favor, introduce un número entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido.")

# Solicitar el género del usuario con validación
def pedir_genero():
    while True:
        genero = input("Introduce tu género ('hombre' o 'mujer'): ").lower()
        if genero in ("hombre", "mujer"):
            return genero
        else:
            print("Género no válido. Por favor, introduce 'hombre' o 'mujer'.")

# Diccionarios para mostrar opciones y recomendaciones
objetivos_texto = {
    1: "Bajar peso",
    2: "Mantener peso",
    3: "Ganar músculo",
    4: "Recomposición corporal"
}

recomendaciones = {
    1: "Para bajar peso, realiza cardio regular y mantén un déficit calórico moderado.",
    2: "Para mantener peso, mantén una dieta equilibrada y actividad física regular.",
    3: "Para ganar músculo, enfócate en entrenamiento de fuerza y un superávit calórico controlado.",
    4: "Para recomposición corporal, combina entrenamiento de fuerza con un ligero déficit calórico y alta ingesta de proteínas."
}

# Solicitar el objetivo del usuario con validación
def pedir_objetivo():
    while True:
        try:
            opcion = int(input("Introduce el número de tu objetivo (1-4): "))
            if opcion in objetivos_texto:
                return opcion
            else:
                print("Por favor, introduce un número entre 1 y 4.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido.")

# Calcula el valor de GET (Gasto Energético Total)
def calcular_get(tmb, factor_actividad):
    return tmb * factor_actividad

# Calcula las calorías diarias recomendadas según el objetivo
def calcular_calorias_objetivo(get, objetivo):
    if objetivo == 1:  
        return get * 0.85
    elif objetivo == 2:  
        return get
    elif objetivo == 3:  
        return get * 1.15
    elif objetivo == 4: 
        return get * 0.90
    else:
        raise ValueError("Objetivo no válido. Por favor, introduce un número válido.")

def main():
    print("¡Bienvenido a la Calculadora de Salud y Rutina!")

    peso = float(input("Introduce tu peso en kg: "))
    altura_cm = float(input("Introduce tu altura en centímetros: "))
    altura_metros = altura_cm / 100 
    edad = int(input("Introduce tu edad en años: "))
    genero = pedir_genero()

    print("\nSelecciona tu objetivo principal:")
    for clave, valor in objetivos_texto.items():
        print(f"{clave}. {valor}")

    objetivo = pedir_objetivo()
    print(f"Has seleccionado: {objetivos_texto[objetivo]}")

    print("\nRecomendación:")
    print(recomendaciones[objetivo])

    imc = calcular_imc(peso, altura_metros)
    interpretacion = interpretar_imc(imc)

    print(f"\nTu índice de masa corporal IMC es: {imc:.2f} ({interpretacion})\n")

    try:
        tmb = calcular_tmb(peso, altura_cm, edad, genero)
        print(f"Tu tasa metabólica basal es: {tmb:.2f} kcal/día")

        mostrar_niveles_actividad()
        nivel = pedir_nivel_actividad()
        factor = obtener_factor_actividad(nivel)
        get = calcular_get(tmb, factor)
        print(f"\nTu gasto energético total estimado es: {get:.2f} kcal/día")

    except ValueError as e:
        print(f"Error: {e}")
        return

    try:
        calorias_objetivo = calcular_calorias_objetivo(get, objetivo)
        print(f"\nCalorías recomendadas para tu objetivo: {calorias_objetivo:.2f} kcal/día")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
