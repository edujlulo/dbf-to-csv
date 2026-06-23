import pandas as pd
import csv

# Load the CSV file
df = pd.read_csv("frases_filtered.csv")

# Valid categories in Spanish
valid_categories = [
    "HIGADO",
    "RAZAS",
    "VESICULA BILIAR",
    "ESTOMAGO",
    "INTESTINO DELGADO",
    "UTERO",
    "PROSTATA",
    "RIÑON IZQUIERDO",
    "INTESTINO GRUESO",
    "BAZO",
    "MOTIVOS",
    "OCULAR",
    "TESTICULOS",
    "RIÑON DERECHO",
    "VEJIGA URINARIA",
    "CONCLUSIONES",
    "TORAX , PULMONES",
    "GLANDULA TIROIDES",
    "GLANDULA MAMARIA",
    "CAVIDAD ABDOMINAL",
    "VEJIGA",
    "MUSCULAR",
    "HUESOS",
    "PANCREAS",
    "OVARIOS",
    "LINFONODOS",
    "GRANDES VASOS, VENAS Y ARTERIA",
    "SEXO",
    "GLANDULAS ADRENALES",
    "URETRA",
    "REFERIDOS",
    "ESPECIES",
    "OBSERVACIONES",
    "COLONOSCOPIA",
    "GRANDES VASOS",
    "GASTROSCOPIA",
    "EQUIPOS",
    "MEDICAMENTO",
    "DIAGNOSTICOS DIFERENCIALES",
    "CADERA",
    "IMPRESION DIAGNOSTICA",
    "RECOMENDACIONES",
]

# Filter rows: keep ONLY valid CAMPO values
filtered_df = df[df["CAMPO"].isin(valid_categories)].copy()

# Rename columns
filtered_df = filtered_df.rename(columns={
    "CAMPO": "category",
    "FRASE": "content"
})

# Clean line breaks
filtered_df["content"] = filtered_df["content"].str.replace("\n", " ", regex=False)

# Sort by category first, then by content
filtered_df = filtered_df.sort_values(
    by=["category", "content"],
    ascending=[True, True]
)

# Save CSV with proper quoting
filtered_df.to_csv(
    "frases_filtradas.csv",
    index=False,
    encoding="utf-8",
    quoting=csv.QUOTE_ALL
)