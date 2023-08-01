import pandas as pd
import zipfile
from scipy import stats as st
import matplotlib.pyplot as plt
import os
import constants as cs


def load_data(filename: str) -> pd.DataFrame:
    with zipfile.ZipFile(f"../{filename}.zip") as data_zip:
        with data_zip.open(f"{filename}.csv") as developer_data:
            return pd.read_csv(developer_data)
        
def main():
    na_data = load_data(cs.NORTH_AMERICA_DATA)

    na_data[cs.EDUCATION].replace(cs.EDUCATION_LEVEL_MAPPING, inplace=True)
    na_data[cs.INDUSTRY].replace(cs.INDUSTRY_MAPPING, inplace=True)
    na_data[cs.COUNTRY].replace(cs.COUNTRY_MAPPING, inplace=True)
    na_data = na_data.drop(columns=[cs.EMPLOYMENT_TYPE, cs.AISENT, cs.REMOTE, cs.CURRENCY, cs.INDEX])


    print(f"Rows before dropping na values {na_data.shape}")
    na_data = na_data.dropna(subset=[cs.COMPENSATION, cs.YEARS_CODE_PRO, cs.YEARS_CODE])
    print(f"Rows after dropping na values {na_data.shape}")


    na_data.to_csv(f"{cs.NA_TRAIN_DATA}.csv", index=False)
    with zipfile.ZipFile(f"../{cs.NA_TRAIN_DATA}.zip", 'w') as zipf:
        zipf.write(f"{cs.NA_TRAIN_DATA}.csv")
    os.remove(f"{cs.NA_TRAIN_DATA}.csv")


if __name__ == "__main__":
    main()
