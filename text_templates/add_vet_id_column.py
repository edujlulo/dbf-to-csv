import pandas as pd

# Doctor: DRA. FRANZISKA GLATZLE

# Load the original CSV file (DO NOT MODIFY IT)
input_file = "default_templates_without_vet_id.csv"

df = pd.read_csv(input_file)

# Add vet_id column with a fixed value for all rows
df["vet_id"] = "da07b0a1-53a8-42db-9c7a-748415bf9734"

# Save to a new CSV file (original file remains unchanged)
output_file = "default_templates_with_vet_id.csv"

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8",
    quoting=1  # csv.QUOTE_ALL
)