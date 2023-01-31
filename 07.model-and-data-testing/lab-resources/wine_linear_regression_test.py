# Databricks notebook source
# MAGIC %md This notebook is slightly modified version of `MLflow Training Tutorial` from [MLflow examples](https://github.com/mlflow/mlflow/tree/master/examples/sklearn_elasticnet_wine).
# MAGIC 
# MAGIC It predicts the quality of wine using [sklearn.linear_model.ElasticNet](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html).
# MAGIC This is a base code and will be modified further during the `Databricks: Reproducible experiments with MLflow and Delta Lake` tutorial.
# MAGIC 
# MAGIC Attribution
# MAGIC * The data set used in this example is from http://archive.ics.uci.edu/ml/datasets/Wine+Quality
# MAGIC * P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
# MAGIC * Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

# COMMAND ----------

# Imports
import os
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

import logging


# COMMAND ----------

# Wine Quality Sample
def train(alpha=0.3, l1_ratio=0.5):

    logging.basicConfig(level=logging.WARN)
    logger = logging.getLogger(__name__)

    def eval_metrics(actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2


    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the wine-quality csv file from the URL
    csv_url =\
        'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
    try:
        data = pd.read_csv(csv_url, sep=';')
    except Exception as e:
        logger.exception(
            "Unable to download training & test CSV, check your internet connection. Error: %s", e)

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    # Execute ElasticNet
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)

    # Evaluate Metrics
    predicted_qualities = lr.predict(test_x)
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)
    
    # Write scores to a file
    with open("metrics.txt", 'w') as outfile:
        outfile.write("  RMSE: %s" % rmse)
        outfile.write("  MAE: %s" % mae)
        outfile.write("  R2: %s" % r2)

train()

# COMMAND ----------


