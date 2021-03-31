# load train file
# train algorithm
# save the matrics and parameters
import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.vector_ar.var_model import VAR
import argparse
import joblib
import json

def eval_matrics(actual,pred):
    rmse =np.sqrt(mean_squared_error(actual,pred))
    return rmse

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    model_dir = config["model_dir"]

    target = config["base"]["target_col"]

    train = pd.read_csv(train_data_path)
    test = pd.read_csv(test_data_path)

    model = VAR(endog=train)
    model_fit = model.fit()

    prediction_quality = model_fit.forecast(model_fit.y,steps=len(test))

    rmse = eval_matrics(test,prediction_quality)



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="parameters.yaml")
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)