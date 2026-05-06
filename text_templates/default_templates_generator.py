import pandas as pd

# Load the CSV file
df = pd.read_csv("frases_filtered.csv")

# Mapping: Spanish -> English
mapping = {
    "HIGADO": "liver",
    "RAZAS": "breed",
    "VESICULA BILIAR": "gallbladder",
    "ESTOMAGO": "stomach",
    "INTESTINO DELGADO": "small_intestine",
    "UTERO": "uterus",
    "PROSTATA": "diagnosis",
    "RIÑON IZQUIERDO": "left_kidney",
    "INTESTINO GRUESO": "colon",
    "BAZO": "spleen",
    "MOTIVOS": "reason_for_ultrasound",
    "OCULAR": "ocular_study",
    "TESTICULOS": "sex",
    "RIÑON DERECHO": "right_kidney",
    "VEJIGA URINARIA": "urinary_bladder",
    "CONCLUSIONES": "conclusions",
    "TORAX , PULMONES": "thorax_lungs",
    "GLANDULA TIROIDES": "thyroid_glands",
    "GLANDULA MAMARIA": "mammary_glands",
    "CAVIDAD ABDOMINAL": "abdominal_cavity",
    "VEJIGA": "urinary_bladder",
    "MUSCULAR": "muscular_study",
    "HUESOS": "bones_others",
    "PANCREAS": "pancreas",
    "OVARIOS": "ovaries",
    "LINFONODOS": "lymph_nodes",
    "GRANDES VASOS, VENAS Y ARTERIA": "major_vessels",
    "SEXO": "sex",
    "GLANDULAS ADRENALES": "adrenal_glands",
    "URETRA": "urethra",
    "REFERIDOS": "referred_by",
    "ESPECIES": "species",
    "OBSERVACIONES": "observations",
    "COLONOSCOPIA": "colon_notes",
    "GRANDES VASOS": "major_vessels",
    "GASTROSCOPIA": "stomach",
    "EQUIPOS": "equipment_used",
    "MEDICAMENTO": "diagnosis",
    "DIAGNOSTICOS DIFERENCIALES": "diagnosis",
    "CADERA": "diagnosis",
    "IMPRESION DIAGNOSTICA": "conclusions",
    "RECOMENDACIONES": "conclusions",
}

# Filter rows: keep ONLY valid CAMPO values
filtered_df = df[df["CAMPO"].isin(mapping.keys())].copy()

# Replace Spanish with English values
filtered_df["CAMPO"] = filtered_df["CAMPO"].map(mapping)

# Rename columns
filtered_df = filtered_df.rename(columns={
    "CAMPO": "category",
    "FRASE": "content"
})

# Clean line breaks
filtered_df["content"] = filtered_df["content"].str.replace("\n", " ", regex=False)

# Save CSV with proper quoting
filtered_df.to_csv(
    "frases_cleaned.csv",
    index=False,
    encoding="utf-8",
    quoting=1  # csv.QUOTE_ALL
)