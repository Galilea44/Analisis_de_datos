from data_loader import DataLoader
from analisis_datos.mayor_reprobacion import MayorReprobacion
from analisis_datos.mayor_promedio import MayorPromedio
from analisis_datos.tendencia import Tendencia
from analisis_datos.riesgo import RiesgoAcademico


def mostrar_menu():
    print("\n--- SISTEMA DE ANÁLISIS ACADÉMICO ---")
    print("1. Materias con mayor índice de reprobación")
    print("2. Carreras con mayor promedio")
    print("3. Tendencias por semestre")
    print("4. Posibles riesgos académicos")
    print("5. Salir")


def main():
    loader = DataLoader("datos.csv")
    df = loader.obtener_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            MayorReprobacion(df).ejecutar()

        elif opcion == "2":
            MayorPromedio(df).ejecutar()

        elif opcion == "3":
            Tendencia(df).ejecutar()

        elif opcion == "4":
            RiesgoAcademico(df).ejecutar()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()