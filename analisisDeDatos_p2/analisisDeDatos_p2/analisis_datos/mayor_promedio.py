class MayorPromedio:

    def __init__(self, df):
        self.df = df

    def ejecutar(self):
        resultado = (
            self.df.groupby("carrera")["calificacion"]
            .mean()
            .sort_values(ascending=False)
        )

        print("\n ---PROMEDIO POR CARRERA: ---")
        print(resultado)