import polars as pl


def add_one_to_col(df: pl.DataFrame, target_col: str) -> pl.DataFrame:
    """
    Add one to the values in the target column.

    :param df: The DataFrame to modify
    :type df: pl.DataFrame
    :param target_col: The column to modify
    :type target_col: str
    :return: The modified DataFrame
    :rtype: pl.DataFrame
    """
    return df.with_columns((pl.col(target_col) + 1).alias(target_col))


def add_a_to_col(df: pl.DataFrame, target_col: str, a: float = 0.0) -> pl.DataFrame:
    """
    Add a value ``a`` to the values in the target column.

    :param df: The DataFrame to modify
    :type df: pl.DataFrame
    :param target_col: The column to modify
    :type target_col: str
    :param a: The value to add
    :type a: float
    :return: The modified DataFrame
    :rtype: pl.DataFrame
    """
    return df.with_columns((pl.col(target_col) + a).alias(target_col))
