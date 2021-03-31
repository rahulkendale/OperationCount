# read thwe data from data source
# save the data in data/raw
import os
from get_data import read_params, get_data
import argparse

def loan_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    raw_data_apth = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_apth,index=False)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="parameters.yaml")
    parsed_args = args.parse_args()
    loan_and_save(config_path=parsed_args.config)