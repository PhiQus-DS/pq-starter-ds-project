import logging

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

# Set up a logger for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler("classifier.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def gridsearch_LR(
    preprocessor: ColumnTransformer,
    C: list[float],
    penalty: list[str],
    solver: list[str],
    max_iter: list[int]
) -> GridSearchCV:
    """
    Creates a GridSearchCV object for logistic regression
    using a given preprocessing pipeline.

    Parameters:
    - preprocessor: Preprocessing steps to apply before classification.
    - C: list of float, inverse regularization strengths to try.
    - penalty: list of str, types of regularization ('l1', 'l2').
    - solver: list of str, solvers to use for optimization.
    - max_iter: list of int, maximum iterations allowed for convergence.

    Returns:
    - GridSearchCV object ready to be fitted on training data.
    """

    # Complete Pipeline, preprocessing + model
    logger.info("Creating Pipeline...")

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('clf', LogisticRegression(class_weight='balanced', random_state=20))
    ])

    param_grid = {
        'clf__C': C,
        'clf__penalty': penalty,
        'clf__solver': solver,
        'clf__max_iter': max_iter
    }

    logger.info(f"Hyperparameter grid: {param_grid}")

    # Perform grid search with 5-fold cross-validation
    logger.info("Starting GridSearchCV...")

    grid = GridSearchCV(
        pipeline,
        param_grid,
        cv=5,
        scoring='accuracy',
        n_jobs=-1
    )

    return grid

def train_model(
    grid: GridSearchCV,
    X_train: pd.DataFrame,
    y_train: pd.Series | np.ndarray,
    X_test: pd.DataFrame,
    y_test: pd.Series | np.ndarray
) -> tuple[Pipeline, pd.DataFrame, pd.Series]:
    """
    Fits the GridSearchCV object on the training data and
    evaluates the best model on test data.

    Parameters:
    - grid: Grid search object returned by `gridsearch_LR`.
    - X_train: Features for training.
    - y_train: Target values for training.
    - X_test: Features for testing.
    - y_test: Target values for testing.

    Returns:
    - best_model: The best model found during grid search.
    """

    # Fit the model on the training set
    grid.fit(X_train, y_train)

    # Log best parameters and CV score
    logger.info(f"Best parameters found: {grid.best_params_}")
    logger.info(f"Best cross-validation score: {grid.best_score_:.4f}")

    # Get the best model from grid search
    best_model = grid.best_estimator_

    # Make predictions on the test set
    y_test_preds = best_model.predict(X_test)

    # Log evaluation metrics
    logger.info("- Evaluation on test set -")
    logger.info(f"Accuracy: {accuracy_score(y_test, y_test_preds):.4f}")
    logger.info("Confusion matrix:\n%s", confusion_matrix(y_test, y_test_preds))
    logger.info("Classification report:\n%s", classification_report(y_test,
                                                                    y_test_preds)
                                                                )

    return best_model

