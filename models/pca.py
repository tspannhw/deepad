#
# @license
# Copyright 2020 Cloudera Fast Forward. https://github.com/fastforwardlabs
# DeepAd: Experiments detecting Anomalies with Deep Neural Networks https://ff12.fastforwardlabs.com/.
# Licensed under the MIT License (the "License");
# =============================================================================
#

# set random seed for reproducibility
from sklearn.decomposition import PCA
import numpy as np
import random
from scipy.spatial.distance import cdist

np.random.seed(2018)
np.random.RandomState(2018)
random.seed(2018)


class PCAModel():
    def __init__():
        self.name = "pca"

    def train(self, in_train, in_val, num_features=2):
        num_features = min(num_features, in_train.shape[1])
        self.model = PCA(n_components=num_features)
        self.model .fit(in_train)
        print("Explained variation per principal component: ",
              np.sum(self.model.explained_variance_ratio_))

    def compute_anomaly_score(self, df):
        low_dim = self.model.transform(df)
        preds = self.model.inverse_transform(low_dim)
        mse = np.mean(np.power(df - preds, 2), axis=1)
        return mse

    def compute_anomaly_score_unsupervised(self, df):
        """Compute anomaly score as distance from learned PCA components

        Arguments:
            df {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        anomaly_scores = np.sum(
            cdist(df, self.model.components_),
            axis=1).ravel()
        return anomaly_scores
