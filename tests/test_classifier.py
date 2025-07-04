from pathlib import Path

import pandas as pd
from pytest import fixture
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.classifier import gridsearch_LR, train_model

# Pytest Fixtures and Tests

@fixture
def load_data_titanic() -> pd.DataFrame:
    """
    Fixture that loads the Titanic dataset file in the data directory.
    """
    data_path = Path(__file__).parent.parent / "data" / "data_sample_titanic.csv"

    return pd.read_csv(data_path)

@fixture
def create_ds(load_data_titanic) -> tuple[pd.DataFrame, pd.Series]:
    """
    Fixture that loads the Titanic dataset and splits it into features (X)
    and target labels (y).
    """
    df = load_data_titanic

    # Features and target
    X = df.drop(columns="Survived")
    y = df["Survived"]

    return X, y

@fixture
def create_preprocessor() -> ColumnTransformer:
    """
    Fixture that returns a preprocessing pipeline for the Titanic dataset
    that scales numerical columns and encodes categorical ones,
    while passing through the rest of the features.
    """
    # Column categories
    num_cols = ['Age', 'Fare']
    bin_cols = ['Sex'] # 'Sex' is binary: male/female
    cat_cols = ['Embarked'] # 'Embarked' is categorical ordinal (S, C, Q)
    passthrough_cols = ['Pclass', 'SibSp', 'Parch']

    # Pipeline for numerical columns
    num_transformer = Pipeline([
    ('scaler', StandardScaler())
    ])

    # Pipeline for binary columns
    bin_transformer = Pipeline([
    ('encoder', OneHotEncoder())
    ])

    cat_transformer = Pipeline([
    ('encoder', OneHotEncoder())
    ])

    # Full column transformer
    preprocessor = ColumnTransformer([
        ('num', num_transformer, num_cols),
        ('bin', bin_transformer, bin_cols),
        ('cat', cat_transformer, cat_cols),
        ('pass', 'passthrough', passthrough_cols)
    ])

    return preprocessor

@fixture
def model_and_test_data(
    create_ds,
    create_preprocessor
) -> tuple[Pipeline, pd.DataFrame, pd.Series]:
    """
    Fixture that trains the model using a preprocessing pipeline and grid search,
    returns a tuple containing the trained model (Pipeline), test features,
    and test labels.
    """
    X, y = create_ds
    preprocessor = create_preprocessor

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=20
    )

    grid = gridsearch_LR(preprocessor,
                         C = [0.001, 0.01, 0.1, 1, 10, 100],
                         penalty = ['l2'],
                         solver = ['liblinear', 'lbfgs'],
                         max_iter = [500, 1000, 2000]
                    )

    model = train_model(grid, X_train, y_train, X_test, y_test)

    return model, X_test, y_test


def test_model_output(model_and_test_data: tuple[Pipeline, pd.DataFrame, pd.Series]):
    """
    Test that the trained model performs reasonably on the test set.

    The test ensures that:
    - The model was returned successfully.
    - The model exposes a `predict` method.
    - The model achieves an accuracy greater than 0.8 on test data.
    """
    model, X_test, y_test = model_and_test_data

    # Ensure model is returned and has the expected interface
    assert model is not None
    assert hasattr(model, 'predict')

    accuracy = model.score(X_test, y_test)

    # Assert that the model reaches a reasonable accuracy threshold
    assert accuracy > 0.8, f"Model accuracy too low: {accuracy:.2f}"
