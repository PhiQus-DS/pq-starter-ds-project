# Reference

In here you can give an overview of your code interfaces or call out important modules.

## A Brief Intro to Autodoc

In the sample `src.deleteme` module you'll find two functions with a [docstring](https://en.wikipedia.org/wiki/Docstring) describing their functionality and arguments. This form of documentation is useful for any developer reading the code, however, we can take it a step further and use this information to build beautiful reference pages for modules, classes, functions or attributes.

We're using [mkdocstrings](https://mkdocstrings.github.io) in this project to allow for this powerful autodoc capability. In order to use it, you simply need:

First, add docstrings to your code, e.g.:

```py
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
```

Then, add the autodoc directive to one of the documentation pages:

```md
# Deleteme Module

::: src.deleteme
```
