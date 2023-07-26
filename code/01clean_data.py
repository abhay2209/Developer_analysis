import pandas as pd
import constants as cs
# import matplotlib.pyplot as plt
from forex_python.converter import CurrencyRates
import zipfile


def load_data() -> pd.DataFrame:
    with zipfile.ZipFile(f"../{cs.DATA_PATH}") as data_zip:
        with data_zip.open(cs.FILENAME) as developer_data:
            return pd.read_csv(developer_data)
        
def filterData(stackoverflow_data: pd.DataFrame, northAmerica: bool) -> pd.DataFrame: 
    result = pd.DataFrame.empty
    if (northAmerica):
        result = stackoverflow_data[((stackoverflow_data[cs.COUNTRY] == cs.CANADA) | (stackoverflow_data[cs.COUNTRY] == cs.USA))]
    else:
        result = stackoverflow_data[~((stackoverflow_data[cs.COUNTRY] == cs.CANADA) | (stackoverflow_data[cs.COUNTRY] == cs.USA))]
    
    return result[(
        (result[cs.MAIN_BRANCH] == cs.DEVELOPERS) & 
        (result[cs.EMPLOYMENT_TYPE].str.contains(cs.EMPLOYED_PART_TIME) | result[cs.EMPLOYMENT_TYPE].str.contains(cs.EMPLOYED_FULL_TIME)) 
        )].drop(cs.MAIN_BRANCH, axis=1).dropna(subset = [cs.COMPENSATION, cs.COMPENSATION], how="all").reset_index()

        
def convertCurrencyToCanadian(currency: str, value: float) -> float:
    if(currency in cs.CURRENCY_CONVERSION_RATE):
        return cs.CURRENCY_CONVERSION_RATE[currency] * value

def getCurrencyCode(data: pd.DataFrame) -> pd.DataFrame:
    data[cs.CURRENCY] = data[cs.CURRENCY].str[:3]
    return data

def main():
    stackoverflow_data = load_data()
    # print(stackoverflow_data.head(5))
    stackoverflow_data = stackoverflow_data[cs.KEEP_COLUMNS]

    # Filtering developers data in north america, employeed full time or part time
    # Convert the currency notations to their code
    north_america = getCurrencyCode(filterData(stackoverflow_data, True))
    rest_of_the_world = getCurrencyCode(filterData(stackoverflow_data, False))

    rest_of_the_world = rest_of_the_world[~rest_of_the_world[cs.CURRENCY].isin(cs.REST_OF_WORLD_CURRENCY_NA)]
    print(rest_of_the_world[cs.COUNTRY].unique())
    print(north_america.shape)
    
    # Convert all compensation values to Canadian dollars
    # Used the below to get all the conversion rates for cad
    # print(CurrencyRates().get_rates(cs.CANADA_CURRENCY))

    north_america[cs.COMPENSATION] = north_america\
        .apply(lambda row: convertCurrencyToCanadian(row[cs.CURRENCY], row[cs.COMPENSATION]), axis=1)
    rest_of_the_world[cs.COMPENSATION] = rest_of_the_world\
        .apply(lambda row: convertCurrencyToCanadian(row[cs.CURRENCY], row[cs.COMPENSATION]), axis=1)
    

if __name__ == "__main__":
    main()