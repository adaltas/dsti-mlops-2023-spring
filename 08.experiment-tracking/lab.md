## Experiment tracking

**Objectives:**

- Demonstrate how experiment tracking helps with linking the code, the results and the environment details.
- Note how this increases the reproducibility.

**Dependencies:**

- notebook to start with: `initial_elasticnet.ipynb`
- notebook to start with: `final_elasticnet.ipynb`

**Instructions:**

1. Install `mlflow`and `sklearn` to your virtual environment: `pip install mlflow sklearn`.
2. Open the `initial_elasticnet.ipynb` with jupyter. Here, you save the metrics of the model in a text file. You can imagine that you could also add additional information about the training and this could be a simple way of implementing experiment tracking. However, the file is overwritten for every run (you would need to add a timestamp to a file name). Even if you do that, imagine how tedious would be to retreive the information. 
3. Modify the notebook to track the model metrics and run information with `mlflow`. Help yourself with the [documentation](https://mlflow.org/docs/latest/tracking.html#id63).
4. Test the different parameters of the model.
5. **Note**: every time that you execute the code, `mlflow` will create a new run in your working directory (`lab-resources`) and save the metrics and other artifacts. You can see it in the working directory, folder `mlruns`.
6. To display the `mlflow dashboard`, go to the terminal to you working directory and run `mlflow ui`. Then open it in your browser on `localhost:5000` and explore it.   
7. Change the model to Random Forest.
8. Track some more experiments and compare the results.
9. Explore the objects, saved by the `mlflow`.

**Schema:**

![Lab schema](./assets/lab_example.png)

**External links:**

- article [Experiment tracking with MLflow on Databricks Community Edition](https://www.adaltas.com/en/2020/09/10/databricks-community-edition-mlflow/)
- article [MLflow tutorial: an open source Machine Learning (ML) platform](https://www.adaltas.com/en/2020/03/23/mlflow-open-source-ml-platform-tutorial/)
