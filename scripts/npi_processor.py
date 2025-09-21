import polars as pl
import pandas as pd
import time

npi_file_path = 'input/npidata_pfile_20050523-20250907.csv'

## just load the first 1000 rows (adjust n_rows if needed)
start_time_polars = time.time()
df_polars = pl.read_csv(npi_file_path)  # you can add n_rows=1000 if you want
end_time_polars = time.time()
elapsed_time_polars = end_time_polars - start_time_polars
print(elapsed_time_polars)

start_time_pandas = time.time()
df_pandas = pd.read_csv(npi_file_path, nrows=1000000, low_memory=False)
end_time_pandas = time.time()
elapsed_time_pandas = end_time_pandas - start_time_pandas
print(elapsed_time_pandas)

print(f"Successfully loaded {len(df_polars)} records from NPI data")
print(f"Columns: {df_polars.columns}")
print(f"\nDataset shape: {df_polars.shape}")
print(f"\nFirst 5 rows:")
print(df_polars.head())
print(f"\nMemory usage (MB): {df_polars.estimated_size() / 1024**2:.2f}")

df_polars_small = df_polars.select([
    'NPI', 
    'Provider Last Name (Legal Name)'
])

## add in a last_updated column
df_polars_small = df_polars_small.with_columns(
    pl.lit('2025-09-03').alias('last_updated')
)

## rename columns: code, description, last_updated
df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
})

## keep only the first 300 rows
df_first300 = df_polars_small.head(300)

## save to csv and parquet
output_path_csv = 'output/npi_small_preview.csv'
output_path_parquet = 'output/npi_small_preview.parquet'

df_first300.write_csv(output_path_csv)
df_first300.write_parquet(output_path_parquet)

print(f"Saved first {len(df_first300)} rows to:")
print(f" - {output_path_csv}")
# print(f" - {output_path_parquet}")
