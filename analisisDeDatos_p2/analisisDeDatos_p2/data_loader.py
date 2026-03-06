import pandas as pd
import os

class DataLoader:

    def __init__(self, nombre_archivo):
        ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
        self.df = pd.read_csv(ruta)
        self.limpiar_datos()

    def limpiar_datos(self):
        # Eliminar filas con valores nulos
        self.df.dropna(inplace=True)

        # Convertir tipos
        self.df["calificacion"] = pd.to_numeric(self.df["calificacion"], errors="coerce")
        self.df["semestre"] = pd.to_numeric(self.df["semestre"], errors="coerce")
        self.df["año"] = pd.to_numeric(self.df["año"], errors="coerce")

        # Eliminar filas incorrectas
        self.df = self.df[self.df["calificacion"].between(0, 10)]

        # Crear columna reprobado
        self.df["reprobado"] = self.df["calificacion"] < 6

    def obtener_datos(self):
        return self.df