#
# @license
# Copyright 2020 Cloudera Fast Forward. https://github.com/fastforwardlabs
# DeepAd: Experiments detecting Anomalies with Deep Neural Networks https://ff12.fastforwardlabs.com/.
# Code samples adapted from https://keras.io/examples/variational_autoencoder/
# Licensed under the MIT License (the "License");
# =============================================================================
#

from data import kdd_data_gen as kdd
import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import logging


def scale_data(df, scaler=None, drop_col="target", dim_size=2):
    df = df.drop(columns=drop_col)
    col_names = df.columns
    if (not scaler):
        scaler = MinMaxScaler(feature_range=(0, 1))
        df = scaler.fit_transform(df)
    else:
        df = scaler.transform(df)

    # df = np.expand_dims(df, axis=dim_size)
    # df = np.expand_dims(df, axis=3)
    return df, scaler, col_names


def load_kdd(data_path="data/kdd", dataset_type="all", partition="all", scaler=None):

    inlier_data_path = os.path.join(
        data_path, partition, dataset_type + "_inliers.csv")
    outlier_data_path = os.path.join(
        data_path, partition, dataset_type + "_outliers.csv")

    if not os.path.exists(os.path.join(inlier_data_path)):
        logging.info(" >> Generating KDD dataset")
        kdd.generate_dataset()

    inliers = pd.read_csv(inlier_data_path)
    outliers = pd.read_csv(outlier_data_path)

    logging.info(" >> KDD dataset loaded")
    inliers, scaler, col_names = scale_data(inliers, scaler=scaler, dim_size=2)
    outliers, _, _ = scale_data(outliers, scaler=scaler, dim_size=2)
    return inliers, outliers, scaler, col_names
