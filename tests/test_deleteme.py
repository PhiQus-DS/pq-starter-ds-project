import polars as pl
from pytest import fixture

from src.deleteme import add_a_to_col, add_one_to_col


@fixture
def df():
    return pl.DataFrame(
        {
            "a": [1, 2, 3, 4, 5],
            "b": [1.0, 2.0, 3.0, 4.0, 5.0],
            "c": ["a", "b", "c", "d", "e"],
        }
    )


def test_add_one_to_col(df):
    result = add_one_to_col(df, "a")
    assert result["a"].to_list() == [2, 3, 4, 5, 6]


def test_add_a_to_col(df):
    result = add_a_to_col(df, "a", 10)
    assert result["a"].to_list() == [11, 12, 13, 14, 15]
