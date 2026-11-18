import csv
import json
import argparse
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "ventas.csv"
def calcular_resumen(ruta_csv=CSV_PATH):
    sedes = {"Lima": 0.0, "Ica": 0.0, "Arequipa": 0.0}
    operaciones = 0
    total_general = 0.0
    with open(ruta_csv, mode="r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            sede = fila["sede"]
            monto = float(fila["total"])
            sedes[sede] = round(sedes.get(sede, 0.0) + monto, 2)
            total_general = round(total_general + monto, 2)
            operaciones += 1
    return {"operaciones": operaciones, "sedes": sedes, "total": total_general}
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resumen de ventas Andina Market 360")
    parser.add_argument("--json", help="Ruta para exportar JSON", default=None)
    args = parser.parse_args()
    res = calcular_resumen()
    if args.json:
        out_path = Path(args.json)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2, ensure_ascii=False)
    print(f"{res['operaciones']} operaciones; Lima {res['sedes']['Lima']:.2f}, Ica {res['sedes']['Ica']:.2f}, Arequipa {res['sedes']['Arequipa']:.2f}, total {res['total']:.2f}")
