# Stage 2 - Prepare CSV for Supabase `text_templates`

## Goal

Transform:

```txt
plantillas_converted.csv
```

into:

```txt
text_templates_full_report_templates.csv
```

ready for your Supabase table:

```sql
public.text_templates
```

## Mapping

Source CSV:

```txt
IDPLANT
NOMBPLAN
INFOPLAN
```

Final CSV:

```txt
vet_id                  <- fixed value
category                <- full_report_template
label                   <- NOMBPLAN
content                 <- empty
full_template_content   <- INFOPLAN
legacy_idplant          <- IDPLANT, only for verification
```

## Important

Your Supabase table does not currently have a `legacy_idplant` column.

So before importing into Supabase, either:

1. Delete the `legacy_idplant` column from the CSV, or
2. Add a temporary/real column to Supabase if you want to preserve the old FoxPro ID.

Recommended for now:

```txt
Keep legacy_idplant while checking the CSV.
Remove it before importing.
```

## Files needed in the same folder

```txt
transform_plantillas_for_supabase.py
plantillas_converted.csv
```

## Install dependencies

```bash
pip install -r requirements.txt
```

Or:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python transform_plantillas_for_supabase.py
```

## Expected output

```txt
text_templates_full_report_templates.csv
```

## Before importing into Supabase

Make sure the CSV columns match your table.

Your current table accepts:

```txt
vet_id
category
label
content
full_template_content
```

Supabase will generate:

```txt
id
created_at
```

`updated_at` can remain empty/null.
