from dbfread import DBF
import pandas as pd
import os

def main():
    print("=== DBF to CSV Converter ===")

    # 1️⃣ Pedir nombre del archivo
    file_name = input("Enter DBF file name (e.g. frases.dbf): ").strip()

    # Verificar que el archivo exista
    if not os.path.exists(file_name):
        print("❌ File not found.")
        return

    # 2️⃣ Leer DBF
    try:
        table = DBF(file_name, encoding="latin1", ignore_missing_memofile=True)
        df = pd.DataFrame(table)
    except Exception as e:
        print("❌ Error reading DBF:", e)
        return

    # 3️⃣ Mostrar columnas disponibles
    print("\nAvailable columns:")
    for col in df.columns:
        print("-", col)

    # 4️⃣ Elegir columnas
    cols_input = input("\nEnter columns separated by comma (or press Enter for all): ").strip()

    if cols_input:
        cols = [c.strip() for c in cols_input.split(",")]

        # Validar columnas
        invalid = [c for c in cols if c not in df.columns]
        if invalid:
            print("❌ Invalid columns:", invalid)
            return

        df = df[cols]

    # 5️⃣ Opcional: modificar datos
    modify = input("\nDo you want to apply basic modifications? (y/n): ").lower()

    if modify == "y":
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].astype(str).str.strip()

        print("✅ Basic cleaning applied (trim spaces).")

    # 6️⃣ Guardar CSV
    output_name = file_name.replace(".dbf", "_filtered.csv")
    df.to_csv(output_name, index=False, encoding="utf-8")

    print(f"\n✅ CSV created successfully: {output_name}")


if __name__ == "__main__":
    main()