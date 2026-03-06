from flask import Flask, render_template
from data_loader import DataLoader

app = Flask(__name__)

@app.route("/")
@app.route("/dashboard")
@app.route("/dashboard/<int:anio>")
def dashboard(anio=None):
    loader = DataLoader("datos.csv")
    df = loader.obtener_datos()

    # Filtrar por año si se especifica
    if anio is not None:
        df = df[df["año"] == anio]

    # Promedio general
    promedio_general = round(df["calificacion"].mean(), 2)

    # Tasa reprobación
    tasa_reprobacion = round((df["calificacion"] < 6).mean() * 100, 2)

    # Materias con mayor reprobación
    materias_reprobacion = (
        df.groupby("materia")["calificacion"]
        .apply(lambda x: (x < 6).mean())
        .sort_values(ascending=False)
        .head(4)
        .to_dict()
    )
    materia_mayor_reprobacion = list(materias_reprobacion.keys())[0] if materias_reprobacion else ""

    # Carreras con mayor promedio
    carreras_promedio = (
        df.groupby("carrera")["calificacion"]
        .mean()
        .sort_values(ascending=False)
        .to_dict()
    )

    # Tendencias por semestre
    tendencias = []
    for (año_sem, semestre), datos in df.groupby(["año", "semestre"]):
        tendencias.append({
            "año": año_sem,
            "semestre": semestre,
            "promedio": round(datos["calificacion"].mean(), 2),
            "estudiantes": len(datos)
        })

    # Alumnos en riesgo
    riesgo = df[df["calificacion"] < 6].copy()  # hacemos copia para no afectar df original
    riesgo["id"] = riesgo.index  # asigna el índice del DataFrame como "id"
    alumnos_riesgo = riesgo.to_dict(orient="records")

    # Variables para Chart.js
    materias_labels = list(materias_reprobacion.keys())
    materias_datos = [round(v*100,2) for v in materias_reprobacion.values()]

    carreras_labels = list(carreras_promedio.keys())
    carreras_datos = [round(v,2) for v in carreras_promedio.values()]

    tendencia_labels = [f"{t['año']} S{t['semestre']}" for t in tendencias]
    tendencia_datos = [t["promedio"] for t in tendencias]

    return render_template(
        "dashboard.html",
        promedio_general=promedio_general,
        tasa_reprobacion=tasa_reprobacion,
        materia_mayor_reprobacion=materia_mayor_reprobacion,
        riesgo_total=len(riesgo),
        materias_reprobacion=materias_reprobacion,
        carreras_promedio=carreras_promedio,
        tendencias=tendencias,
        alumnos_riesgo=alumnos_riesgo,
        # Para gráficas
        materias_labels=materias_labels,
        materias_datos=materias_datos,
        carreras_labels=carreras_labels,
        carreras_datos=carreras_datos,
        tendencia_labels=tendencia_labels,
        tendencia_datos=tendencia_datos
    )


if __name__ == "__main__":
    app.run(debug=True)