class RiesgoAcademico:

    def __init__(self, df):
        self.df = df

    def ejecutar(self):
        print("\n--- POSIBLES RIESGOS ACADÉMICOS ---")

        # 1) Estudiantes con materias reprobadas
        riesgos = (
            self.df[self.df['calificacion'] < 6.0]
            .groupby(['id_estudiante', 'carrera'])
            .size()
        )

        print("\n Estudiantes con materias reprobadas:")

        if not riesgos.empty:
            for (estudiante, carrera), materias in riesgos.items():
                print(f"   Estudiante {estudiante} ({carrera}): {materias} materia(s) reprobada(s)")
        else:
            print("   No hay estudiantes con materias reprobadas.")


        # 2) Promedio bajo
        promedio_estudiante = (
            self.df.groupby("id_estudiante")["calificacion"]
            .mean()
        )

        riesgo_promedio = promedio_estudiante[promedio_estudiante < 6.5]

        print("\n Estudiantes con promedio menor a 6.5:")

        if not riesgo_promedio.empty:
            for estudiante, promedio in riesgo_promedio.items():
                print(f"   Estudiante {estudiante}: Promedio {promedio:.2f}")
        else:
            print("   No hay estudiantes en esta categoría.")


        #  3) Tendencia descendente
        tendencia = (
            self.df.groupby(["id_estudiante", "semestre"])["calificacion"]
            .mean()
            .unstack()
        )

        cambio = tendencia.diff(axis=1).mean(axis=1)
        riesgo_tendencia = cambio[cambio < 0]