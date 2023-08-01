import pandas as pd
import constants as cs
import numpy as np
import matplotlib.pyplot as plt
import zipfile
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, GridSearchCV, ParameterGrid
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, make_scorer
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.compose import TransformedTargetRegressor
from sklearn.neural_network import MLPRegressor
import joblib

def load_data(filename: str) -> pd.DataFrame:
    with zipfile.ZipFile(f"../{filename}.zip") as data_zip:
        with data_zip.open(f"{filename}.csv") as developer_data:
            return pd.read_csv(developer_data)

def custom_accuracy_score(y_true, y_pred):
        accuracy_count = 0
        for true_val, pred_val in zip(y_true, y_pred):
            if abs(true_val - pred_val) <= 15000:
                accuracy_count += 1

        accuracy = accuracy_count / len(y_true)
        return accuracy

def modelPredictAndScore(X_valid, y_valid, model, modelName):
    # Now you can use the loaded model to make predictions on new data
    y_pred_valid = model.predict(X_valid)
    rcustom_score_valid = custom_accuracy_score(y_valid, y_pred_valid)
    # Calculate Root Mean Square Error (RMSE) for training and validation data
    rmse_valid = np.sqrt(mean_squared_error(y_valid, model.predict(X_valid)))

    print(f"{modelName} accuracy is:{rcustom_score_valid}")
    print(f"{modelName} root mean square is:{rmse_valid}")


def main():
    na_data = load_data(cs.NA_TRAIN_DATA)
    X_valid = load_data(cs.X_VALID)
    y_valid = load_data(cs.Y_VALID)

    # scaler_model = joblib.load(f'{cs.ML_MODELS_FOLDER}/scaler.pkl')
    # svr_model = joblib.load(f'{cs.ML_MODELS_FOLDER}/{cs.BEST_SVR_MODELS}.pkl')
    rf_model = joblib.load(f'{cs.ML_MODELS_FOLDER}/{cs.BEST_RF_MODELS}.pkl')
    # gb_model = joblib.load(f'{cs.ML_MODELS_FOLDER}/{cs.BEST_GB_MODELS}.pkl')

    modelPredictAndScore(X_valid, y_valid, rf_model, cs.RANDOM_FOREST_MODELS)
    # modelPredictAndScore(X_valid, y_valid, gb_model, cs.GB_MODELS)
    # X_valid_scaled = scaler_model.transform(X_valid)
    # modelPredictAndScore(X_valid_scaled, y_valid, svr_model, cs.SVR_MODELS)


if __name__ == "__main__":
    main()
