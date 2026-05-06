from dbfread import DBF
import pandas as pd
import csv
from pathlib import Path

DBF_FILE = "plantillas.dbf"
OUTPUT_FILE = "plantillas_converted.csv"

# Try these encodings if accents/ñ look wrong.
# For old FoxPro files, latin1 or cp1252 are common.
ENCODING = "latin1"

# Set to False if you intentionally want to export deleted FoxPro records too.
SKIP_DELETED = True


def clean_text(value):
    """Clean text without destroying multi-line memo content."""
    if value is None:
        return ""

    if isinstance(value, str):
        # Remove spaces at the beginning/end, but preserve internal line breaks.
        return value.strip()

    return value


def main():
    dbf_path = Path(DBF_FILE)
    fpt_path = dbf_path.with_suffix(".FPT")

    print("=== FoxPro DBF + FPT to CSV Converter ===")

    if not dbf_path.exists():
        raise FileNotFoundError(f"DBF file not found: {dbf_path}")

    if not fpt_path.exists():
        print(f"WARNING: Memo file not found: {fpt_path}")
        print("If this DBF has Memo fields, the CSV will not contain the full memo text.")
    else:
        print(f"Memo file found: {fpt_path}")

    # Important:
    # Do NOT use ignore_missing_memofile=True here.
    # This table has a Memo field, so the .FPT file must be read.
    table = DBF(
        dbf_path,
        encoding=ENCODING,
        char_decode_errors="ignore",
        ignore_missing_memofile=False,
        load=True,
    )

    print("\nFields found:")
    for field in table.fields:
        print(f"- {field.name} ({field.type})")

    records = []

    # dbfread usually skips deleted records by default when iterating.
    # This explicit path keeps the intention clear.
    source_records = table if SKIP_DELETED else table.records

    for record in source_records:
        cleaned_record = {key: clean_text(value) for key, value in dict(record).items()}
        records.append(cleaned_record)

    df = pd.DataFrame(records)

    # For this specific table, keep these expected columns if they exist.
    expected_columns = ["IDPLANT", "NOMBPLAN", "INFOPLAN"]
    existing_expected_columns = [col for col in expected_columns if col in df.columns]

    if existing_expected_columns:
        df = df[existing_expected_columns]

    print(f"\nRows exported: {len(df)}")
    print(f"Columns exported: {list(df.columns)}")

    # Basic validation for the Memo column.
    if "INFOPLAN" in df.columns:
        non_empty_memos = df["INFOPLAN"].astype(str).str.strip().ne("").sum()
        print(f"Non-empty INFOPLAN memo values: {non_empty_memos}")

        sample = df["INFOPLAN"].astype(str).str.strip()
        sample = sample[sample.ne("")]
        if not sample.empty:
            print("\nMemo sample:")
            print(sample.iloc[0][:500])

    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8",
        quoting=csv.QUOTE_ALL,
        lineterminator="\n",
    )

    print(f"\nCSV created successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
