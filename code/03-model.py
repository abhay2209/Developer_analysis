import pandas as pd
import constants as cs
import numpy as np
import matplotlib.pyplot as plt
import zipfile
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def load_data(filename: str) -> pd.DataFrame:
    with zipfile.ZipFile(f"../{filename}.zip") as data_zip:
        with data_zip.open(f"{filename}.csv") as developer_data:
            return pd.read_csv(developer_data)


X_train, X_valid, y_train, y_valid = train_test_split(X, y)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
print(model.score(X_train, y_train))
print(model.score(X_valid, y_valid))

def main():
    na_data = load_data(cs.NORTH_AMERICA_DATA)


if __name__ == "__main__":
    main()







