def save_to_formats(df, base_filename):
    """
    Save the DataFrame to CSV and Parquet formats.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    base_filename (str): The base filename without extension.
    """
    csv_filename = f"{base_filename}.csv"
    parquet_filename = f"{base_filename}.parquet"

    df.to_csv(csv_filename, index=False)
    df.to_parquet(parquet_filename, index=False)