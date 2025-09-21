import polars as pl
from pathlib import Path

file_path = Path('input/sct2_Description_Full-en_US1000124_20250901.txt')

df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

output_dir = Path('output')
output_dir.mkdir(exist_ok=True)

# Only keep first 300 rows
df_first300 = df.head(300)

output_path = output_dir / 'sct2_Description_Full_preview.csv'
df_first300.write_csv(output_path)

print(f"Successfully saved first {len(df_first300)} records from SNOMED CT file")
print(f"Saved to {output_path}")
print(f"Preview shape: {df_first300.shape}")
print(f"\nColumn names: {df_first300.columns}")
print(f"\nFirst 5 rows:")
print(df_first300.head())
print(f"\nMemory usage (MB): {df_first300.estimated_size() / 1024**2:.2f}")

print(f"\nActive terms count in preview: {df_first300.filter(pl.col('active') == 1).height}")
print(f"Language codes in preview: {df_first300['languageCode'].unique().to_list()}")
