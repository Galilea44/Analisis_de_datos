class MayorReprobacion:

    def __init__(self, df):
        self.df = df

    def ejecutar(self):
        print("\n--- MATERIAS CON MAYOR ÍNDICE DE REPROBACIÓN ---")
        # Ya existe la columna 'reprobado'
        reprobacion = (
            self.df.groupby('materia')['reprobado']
            .mean()
            .sort_values(ascending=False)
        )

        if not reprobacion.empty:
            for materia, porcentaje in reprobacion.items():
                print(f"   {materia}: {porcentaje * 100:.1f}% de reprobación")
        else:
            print("   No hay materias con reprobación")
