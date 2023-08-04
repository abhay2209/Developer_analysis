# Steps to run
In your repository's README (or README.md) file, you should document your code and how to run it: required libraries, commands (and arguments), order of execution, files produced/expected. You should do this because (1) you should always do that, and (2) to give us some hope of running your code.

## Required modules: 
There are a number of modules that we used in addition to the standard data science libraries in Python. Below is a comprehensive list of the libraries, along with the important versions of each one. 
Uncommon ones are marked with * which might need installing
1. pandas
2. numpy
3. sklearn
4. * xgboost 
5. mathplotlib
6. zipfile
7. joblib
8. statsmodel
9. scipy

To load the models, use the mentioned version for the modules below:
1. sklearn version = 1.0.2
2. xgboost version = 1.7.6


## Steps to follow: 
All datasets created have been saved to be used for the next step. The best machine learning models have been saved so the grid search doesn't have to run again
Raw data: `data_compress.zip`

1. **Data Cleaning**

To run the clean data step, enter the ```code``` directory and run the following command:

```python 01clean_data.py```

This step will pull data from `data_compressed` and create the `north_america.zip` folder, which contains all the cleaned data pertaining to developers in North America. The `rest_of_the_world.zip` contains data on developers outside of North America, which may be useful to you but was not used in our analysis or ML training and models. 

2. **Data Analysis**. 
   This step extracts the cleaned data from `north_america.zip`, and will recreate the graphs used in our report under the `diagram` folder

```python 02-analysis_NA.py```

3. **Feature Engineering** 

To create data for Machine Learning models. This file essentially maps strings to integers, such as industry, education level etc. The created zip file is called `north_america_train.zip` which is already available. 

```python 03-prepare_train.py```

4. Running the Grid Search for Machine Learning models requires to run the `04-model_train.ipynb`. This notebook will create the graphs for validation and accuracy score in ml_models directory while saving the best models (that we selected as graphs were almost consistent each run). It will also save the training and validation data used for those models. The current `X_train_data.zip`, `X_valid_data.zip`, `y_train_data.zip`, and `y_valid_data.zip` is from our previous run. 

5. Model comparison. Once the models have been trained, you may run through `model_comparison.ipynb` Jupyter Notebook step by step. It will load the best models created, create an accuracy score based on $40,000 range compared to model training which uses $30,000. it will also calculate mean absolute error for each models and then create Voting Regressor model using them. Feel free to play around the accuracy score range. 

### Running each individual ML model

If you would like to load an ML model into your own custom environment, simply use the `joblib` python library to load a model from the `ml_model` folder. 



