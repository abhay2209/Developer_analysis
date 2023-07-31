import pandas as pd
import constants as cs
import numpy as np
import matplotlib.pyplot as plt
import zipfile
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.compose import TransformedTargetRegressor
from sklearn.neural_network import MLPRegressor

def load_data(filename: str) -> pd.DataFrame:
    with zipfile.ZipFile(f"../{filename}.zip") as data_zip:
        with data_zip.open(f"{filename}.csv") as developer_data:
            return pd.read_csv(developer_data)

def main():
    na_data = load_data(cs.NORTH_AMERICA_DATA)

    na_data = na_data[[cs.WORK_EXPERIENCE, cs.YEARS_CODE, cs.YEARS_CODE_PRO, cs.COMPENSATION]]

    na_data[cs.YEARS_CODE] = pd.to_numeric(na_data[cs.YEARS_CODE], errors='coerce')
    na_data[cs.WORK_EXPERIENCE] = pd.to_numeric(na_data[cs.WORK_EXPERIENCE], errors='coerce')
    na_data[cs.YEARS_CODE_PRO] = pd.to_numeric(na_data[cs.YEARS_CODE_PRO], errors='coerce')
    na_data[cs.COMPENSATION] = pd.to_numeric(na_data[cs.COMPENSATION], errors='coerce')
    na_data = na_data.dropna(subset=[cs.WORK_EXPERIENCE, cs.COMPENSATION, cs.YEARS_CODE_PRO, cs.YEARS_CODE])

    compensation = na_data[cs.COMPENSATION]
    X_data = na_data[[cs.WORK_EXPERIENCE, cs.YEARS_CODE ,cs.YEARS_CODE_PRO]]

    X_train, X_valid, y_train, y_valid = train_test_split(X_data, compensation)

    # Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_valid_scaled = scaler.transform(X_valid)

    # Random Forest Regressor
    rf_param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [3, 5, 10],
        'min_samples_leaf': [1, 5, 10]
    }
    rf_model = RandomForestRegressor()
    rf_grid_search = GridSearchCV(rf_model, rf_param_grid, cv=5, scoring='neg_mean_squared_error')
    rf_grid_search.fit(X_train, y_train)
    best_rf_params = rf_grid_search.best_params_

    rf_model = RandomForestRegressor(**best_rf_params)
    rf_model.fit(X_train, y_train)
    rf_y_pred_train = rf_model.predict(X_train)
    rf_y_pred_valid = rf_model.predict(X_valid)
    rf_mse_train = mean_squared_error(y_train, rf_y_pred_train)
    rf_mse_valid = mean_squared_error(y_valid, rf_y_pred_valid)
    rf_rmse_train = np.sqrt(rf_mse_train)
    rf_rmse_valid = np.sqrt(rf_mse_valid)
    rf_r2_train = r2_score(y_train, rf_y_pred_train)
    rf_r2_valid = r2_score(y_valid, rf_y_pred_valid)

    print("Best Hyperparameters for Random Forest:", best_rf_params)
    print("Random Forest - R-squared score on training data:", rf_r2_train)
    print("Random Forest - R-squared score on validation data:", rf_r2_valid)
    print("Random Forest - Root Mean Squared Error on training data:", rf_rmse_train)
    print("Random Forest - Root Mean Squared Error on validation data:", rf_rmse_valid)

    # Gradient Boosting Regressor
    gb_param_grid = {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.05, 0.1],
        'max_depth': [3, 5, 10]
    }
    gb_model = GradientBoostingRegressor()
    gb_grid_search = GridSearchCV(gb_model, gb_param_grid, cv=5, scoring='neg_mean_squared_error')
    gb_grid_search.fit(X_train, y_train)
    best_gb_params = gb_grid_search.best_params_

    gb_model = GradientBoostingRegressor(**best_gb_params)
    gb_model.fit(X_train, y_train)
    gb_y_pred_train = gb_model.predict(X_train)
    gb_y_pred_valid = gb_model.predict(X_valid)
    gb_mse_train = mean_squared_error(y_train, gb_y_pred_train)
    gb_mse_valid = mean_squared_error(y_valid, gb_y_pred_valid)
    gb_rmse_train = np.sqrt(gb_mse_train)
    gb_rmse_valid = np.sqrt(gb_mse_valid)
    gb_r2_train = r2_score(y_train, gb_y_pred_train)
    gb_r2_valid = r2_score(y_valid, gb_y_pred_valid)

    print("Best Hyperparameters for Gradient Boosting:", best_gb_params)
    print("Gradient Boosting - R-squared score on training data:", gb_r2_train)
    print("Gradient Boosting - R-squared score on validation data:", gb_r2_valid)
    print("Gradient Boosting - Root Mean Squared Error on training data:", gb_rmse_train)
    print("Gradient Boosting - Root Mean Squared Error on validation data:", gb_rmse_valid)

    # Support Vector Regressor
    svr_param_grid = {
        'C': [1, 10, 100],
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'gamma': ['scale', 'auto']
    }
    svr_model = SVR()
    svr_grid_search = GridSearchCV(svr_model, svr_param_grid, cv=5, scoring='neg_mean_squared_error')
    svr_grid_search.fit(X_train_scaled, y_train)
    best_svr_params = svr_grid_search.best_params_

    svr_model = SVR(**best_svr_params)
    svr_model.fit(X_train_scaled, y_train)
    svr_y_pred_train = svr_model.predict(X_train_scaled)
    svr_y_pred_valid = svr_model.predict(X_valid_scaled)
    svr_mse_train = mean_squared_error(y_train, svr_y_pred_train)
    svr_mse_valid = mean_squared_error(y_valid, svr_y_pred_valid)
    svr_rmse_train = np.sqrt(svr_mse_train)
    svr_rmse_valid = np.sqrt(svr_mse_valid)
    svr_r2_train = r2_score(y_train, svr_y_pred_train)
    svr_r2_valid = r2_score(y_valid, svr_y_pred_valid)

    print("Best Hyperparameters for Support Vector Regressor:", best_svr_params)
    print("Support Vector Regressor - R-squared score on training data:", svr_r2_train)
    print("Support Vector Regressor - R-squared score on validation data:", svr_r2_valid)
    print("Support Vector Regressor - Root Mean Squared Error on training data:", svr_rmse_train)
    print("Support Vector Regressor - Root Mean Squared Error on validation data:", svr_rmse_valid)

    # Neural Network (MLPRegressor)
    nn_param_grid = {
        'hidden_layer_sizes': [(100,), (200,), (100, 100), (200, 100)],
        'activation': ['relu', 'tanh'],
        'alpha': [0.0001, 0.001, 0.01],
        'learning_rate': ['constant', 'invscaling', 'adaptive']
    }
    nn_model = MLPRegressor(max_iter=1000)
    nn_grid_search = GridSearchCV(nn_model, nn_param_grid, cv=5, scoring='neg_mean_squared_error')
    nn_grid_search.fit(X_train_scaled, y_train)
    best_nn_params = nn_grid_search.best_params_

    nn_model = MLPRegressor(max_iter=1000, **best_nn_params)
    nn_model.fit(X_train_scaled, y_train)

    # Perform inverse transformation on the target variable for evaluation
    nn_regressor = TransformedTargetRegressor(regressor=nn_model, transformer=scaler)
    nn_regressor.fit(X_train, y_train)

    # Model evaluation for the Neural Network
    nn_y_pred_train = nn_regressor.predict(X_train)
    nn_y_pred_valid = nn_regressor.predict(X_valid)
    nn_mse_train = mean_squared_error(y_train, nn_y_pred_train)
    nn_mse_valid = mean_squared_error(y_valid, nn_y_pred_valid)
    nn_rmse_train = np.sqrt(nn_mse_train)
    nn_rmse_valid = np.sqrt(nn_mse_valid)
    nn_r2_train = r2_score(y_train, nn_y_pred_train)
    nn_r2_valid = r2_score(y_valid, nn_y_pred_valid)

    print("Best Hyperparameters for Neural Network:", best_nn_params)
    print("Neural Network - R-squared score on training data:", nn_r2_train)
    print("Neural Network - R-squared score on validation data:", nn_r2_valid)
    print("Neural Network - Root Mean Squared Error on training data:", nn_rmse_train)
    print("Neural Network - Root Mean Squared Error on validation data:", nn_rmse_valid)

if __name__ == "__main__":
    main()
