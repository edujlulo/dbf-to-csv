import pandas as pd
import csv
from pathlib import Path

INPUT_FILE = "plantillas_converted.csv"
OUTPUT_FILE = "text_templates_full_report_templates.csv"

VET_ID = "ddf49cb2-ba19-4030-9194-5de45bac1e5e"
CATEGORY = "full_report_template"


def clean_text(value):
    """Clean basic text values while preserving internal line breaks."""
    if pd.isna(value):
        return ""

    return str(value).strip()


def main():
    input_path = Path(INPUT_FILE)

    if not input_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {INPUT_FILE}")

    df = pd.read_csv(input_path, dtype=str)

    required_columns = ["IDPLANT", "NOMBPLAN", "INFOPLAN"]
    missing_columns = [column for column in required_columns if column not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Create the output DataFrame using the same index as the input DataFrame.
    # This is important so fixed values like vet_id and category are repeated for every row.
    output_df = pd.DataFrame(index=df.index)

    # Supabase will generate id automatically, so we do not include it.
    output_df["vet_id"] = VET_ID
    output_df["category"] = CATEGORY
    output_df["label"] = df["NOMBPLAN"].apply(clean_text)

    # The large template goes into full_template_content.
    output_df["full_template_content"] = df["INFOPLAN"].apply(clean_text)

    # Remove rows without a label and without full template content.
    output_df = output_df[
        output_df["label"].str.strip().ne("") |
        output_df["full_template_content"].str.strip().ne("")
    ].copy()

    output_df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8",
        quoting=csv.QUOTE_ALL,
        lineterminator="\n",
    )

    print("CSV created successfully.")
    print(f"Input rows: {len(df)}")
    print(f"Output rows: {len(output_df)}")
    print(f"Output file: {OUTPUT_FILE}")

    print("\nValidation:")
    print(f"Rows with empty vet_id: {(output_df['vet_id'].str.strip() == '').sum()}")
    print(f"Rows with empty category: {(output_df['category'].str.strip() == '').sum()}")

    print("\nColumns generated:")
    for column in output_df.columns:
        print(f"- {column}")


if __name__ == "__main__":
    main()
