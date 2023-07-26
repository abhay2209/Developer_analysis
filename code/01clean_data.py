import pandas as pd
import constants as cs
import zipfile



def load_data() -> pd.DataFrame:
    with zipfile.ZipFile(f"../{cs.DATA_PATH}") as data_zip:
        with data_zip.open(cs.FILENAME) as developer_data:
            return pd.read_csv(developer_data)

def main():
    stackoverflow_data = load_data()
    # print(stackoverflow_data.head(5))
    stackoverflow_data = stackoverflow_data[cs.KEEP_COLUMNS]
    # print(stackoverflow_data['Country'].unique())

    # Filtering developers data in north america
    stackoverflow_data = stackoverflow_data[(
        (stackoverflow_data[cs.MAIN_BRANCH] == cs.DEVELOPERS) & 
        ((stackoverflow_data[cs.COUNTRY] == cs.CANADA) | (stackoverflow_data[cs.COUNTRY] == cs.USA))
        )]
    
    print(stackoverflow_data.shape)
    
    

if __name__ == "__main__":
    main()