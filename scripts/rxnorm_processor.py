import polars as pl
from pathlib import Path

# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

file_path = Path('input/RXNATOMARCHIVE.RRF')

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

output_dir = Path('output')
output_dir.mkdir(exist_ok=True)

# Only keep first 300 rows
df_first300 = df.head(300)

output_path = output_dir / 'RXNATOMARCHIVE_preview.csv'
df_first300.write_csv(output_path)

print(f"Successfully saved first {len(df_first300)} rows to {output_path}")
print(f"Preview shape: {df_first300.shape}")
