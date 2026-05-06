# Stage 1 - Convert `plantillas.dbf` + `plantillas.FPT` to CSV

## Goal

Convert the FoxPro table:

- `plantillas.dbf`
- `plantillas.FPT`

into:

- `plantillas_converted.csv`

The `.CDX` file is not needed for this conversion. It is an index file.

## Why this script is different from the previous one

Your previous script used:

```python
ignore_missing_memofile=True
```

For this table, that is risky because `INFOPLAN` is a Memo field. The real long text is stored in `plantillas.FPT`.

This new script uses:

```python
ignore_missing_memofile=False
```

So Python must read the `.FPT` file.

## Files needed in the same folder

Put these files together:

```txt
convert_plantillas_dbf_to_csv.py
plantillas.dbf
plantillas.FPT
```

Optional:

```txt
plantillas.CDX
```

## Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install dbfread pandas
```

## Run

```bash
python convert_plantillas_dbf_to_csv.py
```

## Expected output

```txt
plantillas_converted.csv
```

## What to check after running

Open the CSV and check that `INFOPLAN` contains real text, not just numbers.

Correct:

```txt
"MOTIVO DEL ESTUDIO ECOGRAFICO..."
```

Incorrect:

```txt
"12345"
```

If you see only numbers in `INFOPLAN`, the `.FPT` memo file was not read correctly.
