import pandas as pd
import constants as cs
# import matplotlib.pyplot as plt
# from forex_python.converter import CurrencyRates
import zipfile
import os

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

def splitDataIntoCols(data: pd.DataFrame, col_name: str, top_x: int)->pd.DataFrame:
    counts = data[col_name].str.split(';').explode().value_counts()
    top_x = counts.index[:top_x]
    top_x_col_data = data[col_name].str.get_dummies(sep=';')[top_x]   
    return top_x_col_data


def main():
    stackoverflow_data = load_data()
    # print(stackoverflow_data.head(5))
    stackoverflow_data = stackoverflow_data[cs.KEEP_COLUMNS]

    # Filtering developers data in north america, employeed full time or part time
    # Convert the currency notations to their code
    north_america = getCurrencyCode(filterData(stackoverflow_data, True))
    rest_of_the_world = getCurrencyCode(filterData(stackoverflow_data, False))

    rest_of_the_world = rest_of_the_world[~rest_of_the_world[cs.CURRENCY].isin(cs.REST_OF_WORLD_CURRENCY_NA)]
    # print(rest_of_the_world[cs.COUNTRY].unique())
    # print(north_america.shape)
    
    # Convert all compensation values to Canadian dollars
    # Used the below to get all the conversion rates for cad
    # print(CurrencyRates().get_rates(cs.CANADA_CURRENCY))
    north_america[cs.COMPENSATION] = north_america\
        .apply(lambda row: convertCurrencyToCanadian(row[cs.CURRENCY], row[cs.COMPENSATION]), axis=1)
    rest_of_the_world[cs.COMPENSATION] = rest_of_the_world\
        .apply(lambda row: convertCurrencyToCanadian(row[cs.CURRENCY], row[cs.COMPENSATION]), axis=1)

    # Split data into columns (Languages, Databases, Frameworks, Tools, Platforms, Other tech. )
    north_america = pd.concat([north_america, 
                                          splitDataIntoCols(north_america, cs.LANGUAGES, cs.TOP_10_LANG),
                                          splitDataIntoCols(north_america, cs.DATABASES, cs.TOP_10_DATABASE),
                                          splitDataIntoCols(north_america, cs.TOOLS, cs.TOP_10_TOOLS),
                                          splitDataIntoCols(north_america, cs.FRAMEWORKS, cs.TOP_10_FRAMEWORKS),
                                          splitDataIntoCols(north_america, cs.PLATFORMS, cs.TOP_10_PLATFORM),
                                          splitDataIntoCols(north_america, cs.OTHER_TECH, cs.TOP_10_OTHER_TECH)], axis = 1)
    
    
    rest_of_the_world = pd.concat([rest_of_the_world, 
                                   splitDataIntoCols(rest_of_the_world, cs.LANGUAGES, cs.TOP_10_LANG),
                                   splitDataIntoCols(rest_of_the_world, cs.DATABASES, cs.TOP_10_DATABASE),
                                   splitDataIntoCols(rest_of_the_world, cs.TOOLS, cs.TOP_10_TOOLS),
                                   splitDataIntoCols(rest_of_the_world, cs.FRAMEWORKS, cs.TOP_10_FRAMEWORKS),
                                   splitDataIntoCols(rest_of_the_world, cs.PLATFORMS, cs.TOP_10_PLATFORM),
                                   splitDataIntoCols(rest_of_the_world, cs.OTHER_TECH, cs.TOP_10_OTHER_TECH)], axis = 1)

    # How is AI used by devs
    ai_use_na =  north_america[cs.USING_AI].str.get_dummies(sep=';')    
    north_america = pd.concat([north_america, ai_use_na], axis =1)

    ai_use_rest = rest_of_the_world[cs.USING_AI].str.get_dummies(sep=';')       
    rest_of_the_world = pd.concat([rest_of_the_world, ai_use_rest
                                   ], axis =1)

    north_america.drop(columns=cs.DROP_TECHNOLOGIES_LIST, axis=1)
    rest_of_the_world.drop(columns=cs.DROP_TECHNOLOGIES_LIST, axis=1)
    
    # What is the top paying skill in each category?
    

    # How do these skills correlate with each other?
    

    north_america.to_csv(f"{cs.NORTH_AMERICA_DATA}.csv", index=False)
    with zipfile.ZipFile(f"../{cs.NORTH_AMERICA_DATA}.zip", 'w') as zipf:
        zipf.write(f"{cs.NORTH_AMERICA_DATA}.csv")

    rest_of_the_world.to_csv(f"{cs.REST_OF_THE_WORLD_DATA}.csv", index=False)
    with zipfile.ZipFile(f"../{cs.REST_OF_THE_WORLD_DATA}.zip", 'w') as zipf:
        zipf.write(f"{cs.REST_OF_THE_WORLD_DATA}.csv")

    os.remove(f"{cs.NORTH_AMERICA_DATA}.csv")
    os.remove(f"{cs.REST_OF_THE_WORLD_DATA}.csv")

if __name__ == "__main__":
    main()