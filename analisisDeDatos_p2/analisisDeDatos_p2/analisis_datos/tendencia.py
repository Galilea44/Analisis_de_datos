class Tendencia:

    def __init__(self, df):
        self.df = df

    def ejecutar(self):
        print("\n--- TENDENCIAS POR SEMESTRE ---")

        # Agrupar SOLO por semestre
        tendencia = (
            self.df.groupby("semestre")
            .agg(
                promedio=("calificacion", "mean"),
                total_estudiantes=("id_estudiante", "nunique")
            )
            .reset_index()
            .sort_values("semestre")
        )

        for _, fila in tendencia.iterrows():
            print(
                f"   Semestre {int(fila['semestre'])}: "
                f"Promedio={fila['promedio']:.2f} | "
                f"Estudiantes={int(fila['total_estudiantes'])}"
            )