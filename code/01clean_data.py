import pandas as pd
import constants as cs
import zipfile


def load_data() -> pd.DataFrame:
    with zipfile.ZipFile(f"../{cs.DATA_PATH}") as data_zip:
   
        with data_zip.open(cs.FILENAME) as developer_data:
            return pd.read_csv(developer_data)

def main():
    stackoverflow_data = load_data()
    print(stackoverflow_data.head(5))



if __name__ == "__main__":
    main()