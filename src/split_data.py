# split raw data
# save it in dat/process folder
import os
import argparse
import pandas as pd
from get_data import read_params,get_data

def convert_to_date(config_path):
    df = get_data(config_path)
    df["CompletedDate"] = pd.to_datetime(df.CompletedDate)
    data = df.drop(["CompletedDate"],axis=1)
    data.index = df.CompletedDate
    return data

def split_and_saved_data(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    #split_ratio = ["split_data"]["train_size"]

    data = convert_to_date(config_path)

    #train = data[:int(split_ratio * (len(data)))]
    #test = data[int(split_ratio * (len(data))):]

    train = data[:int(0.8 * (len(data)))]
    test = data[int(0.8 * (len(data))):]

    train.to_csv(train_data_path,encoding='utf-8')
    test.to_csv(test_data_path,encoding='utf-8')

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="parameters.yaml")
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)



