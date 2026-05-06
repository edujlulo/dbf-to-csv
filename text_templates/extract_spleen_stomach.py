import pandas as pd

# Load the CSV file
df = pd.read_csv("frases_filtered.csv")

# Filter rows
filtered_df = df[df["CAMPO"].isin(["BAZO", "ESTOMAGO"])].copy()

# Replace values
filtered_df["CAMPO"] = filtered_df["CAMPO"].replace({
    "BAZO": "spleen",
    "ESTOMAGO": "stomach"
})

# Add vet_id
filtered_df["vet_id"] = "da07b0a1-53a8-42db-9c7a-748415bf9734"

# Rename columns
filtered_df = filtered_df.rename(columns={
    "CAMPO": "category",
    "FRASE": "content"
})

# Clean line breaks
filtered_df["content"] = filtered_df["content"].str.replace("\n", " ", regex=False)

# ✅ IMPORTANT: force proper CSV quoting
filtered_df.to_csv(
    "frases_spleen_stomach.csv",
    index=False,
    encoding="utf-8",
    quoting=1  # csv.QUOTE_ALL
)