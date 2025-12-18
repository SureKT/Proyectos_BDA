import pandas as pd
import os
import glob

# List of folders to search for CSV files
input_folder = ['C:\SSD_Storage\Sure_Programming\IABD\BDA\AnalisisAcademico']

def convert_csv_to_parquet_in_folders(folders):
    """
    Converts all CSV files in a list of folders to Parquet format.
    The Parquet files are saved in a 'parquet' subfolder within each original folder.
    """
    for folder in folders:
        output_dir = os.path.join(folder, 'parquet')
        os.makedirs(output_dir, exist_ok=True)

        # Find all CSV files in the current folder
        for csv_file in glob.glob(os.path.join(folder, '*.csv')):
            try:
                # Special handling for files that use a semicolon delimiter
                if os.path.basename(csv_file) == 'Indicadores_Finales.csv':
                    df = pd.read_csv(csv_file, sep=';', engine='python')
                else:
                    df = pd.read_csv(csv_file)
                parquet_file = os.path.join(output_dir, os.path.basename(csv_file).replace('.csv', '.parquet'))
                df.to_parquet(parquet_file, index=False)
                print(f"Converted {csv_file} to {parquet_file}")
            except Exception as e:
                print(f"Error converting {csv_file}: {e}")

if __name__ == "__main__":
    convert_csv_to_parquet_in_folders(input_folder)