"""
NormaLex - Generador de datos
Ejecutar: python generate_data.py
Lee BD_LIMPIOS.xlsx y genera los JSON que consume index.html
"""
import json, os
import pandas as pd
from collections import Counter

EXCEL = os.path.join("data", "BD_LIMPIOS.xlsx")
OUT = "data"

def main():
    print("NormaLex — Generando datos...")
    xls = pd.ExcelFile(EXCEL)

    inst = pd.read_excel(xls, sheet_name="INSTRUMENTOS").fillna("")
    instrumentos = []
    for _, r in inst.iterrows():
        d = {"id":r["ID"], "tipo":str(r["Tipo_Instrumento"]), "ciclo":str(r["Ciclo_de_Vida"]),
             "fuente":str(r["Fuente"]), "titulo":str(r["Titulo"])[:200], "cat":str(r["Categoría"]),
             "fecha":str(r["Fecha_Detección"]), "link":str(r["Link"])}
        if r["Identificador_Oficial"]: d["ref"] = str(r["Identificador_Oficial"])[:80]
        if r["Subcategoría"]: d["subcat"] = str(r["Subcategoría"])
        if r["Estado"]: d["estado"] = str(r["Estado"])
        if r["Grupo_Parlamentario"]: d["gp"] = str(r["Grupo_Parlamentario"])
        if r["Fecha_Publicación"]: d["fechaPub"] = str(r["Fecha_Publicación"])
        if r["Fecha_Vigencia"]: d["fechaVig"] = str(r["Fecha_Vigencia"])
        if r["Resumen"]:
            d["resumen"] = str(r["Resumen"])
        instrumentos.append(d)

    ev = pd.read_excel(xls, sheet_name="EVENTOS").fillna("")
    eventos = []
    for _, r in ev.iterrows():
        d = {"id":r["ID_Evento"], "plRef":str(r["PL_Referencia"]), "tipo":str(r["Tipo_Evento"]),
             "fecha":str(r["Fecha_Evento"]), "fuente":str(r["Fuente_Evento"]),
             "titulo":str(r["Titulo_Evento"])[:200]}
        if r["Link"]: d["link"] = str(r["Link"])
        if r["Resumen_Evento"]:
            d["resumen"] = str(r["Resumen_Evento"])
        eventos.append(d)

    stats = {
        "total": len(instrumentos),
        "por_ciclo": dict(Counter(i["ciclo"] for i in instrumentos)),
        "por_fuente": dict(Counter(i["fuente"] for i in instrumentos).most_common(12)),
        "por_categoria": dict(Counter(i["cat"] for i in instrumentos if i["cat"]).most_common(15)),
        "por_tipo": dict(Counter(i["tipo"] for i in instrumentos).most_common(15)),
        "por_estado": dict(Counter(i.get("estado","") for i in instrumentos if i.get("estado"))),
        "total_eventos": len(eventos),
    }

    def write(name, data):
        p = os.path.join(OUT, name)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(",",":"))
        print(f"  {name}: {os.path.getsize(p)/1024:.0f} KB")

    write("instrumentos.json", instrumentos)
    write("eventos.json", eventos)
    write("stats.json", stats)
    print(f"\nListo. {len(instrumentos)} instrumentos, {len(eventos)} eventos.")
    print("Ejecuta: python server.py")

if __name__ == "__main__":
    main()
