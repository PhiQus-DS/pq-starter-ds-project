![pq-banner](.github/img/pq-banner.jpg)

# PhiQus Starter DS Project Repo

Welcome to our Data Science Starter Project template! Here at PhiQus we'd like to share a part of our project workflow: how we structure a repo at a high level. We think that working on a team efficiently requires to have a couple of standards and tools to keep everyone on the same page, and let the team focus on the important task, doing data science!

This repo is designed as a go-to starter kit to help you setup your environment for working on data science projects. It uses python tools for dependency management, code documentation, and even has a starter Pull Request validation

## Features

- **Package and depdency management:** The cornerstone of this template is [poetry](https://python-poetry.org/). Poetry is a powerful tool for dependency and package management, it helps with keeping a clean python environment for each project, but it also takes care of package publishing in case that's part of your workflow.
- **Project documentation:** We use [mkdocs.org](https://www.mkdocs.org) to generate project documentation, including autodocumenting modules, classes, functions or attributes that have [docstrings](https://en.wikipedia.org/wiki/Docstring). This docs can be compiled to html and published anywhere you need them to be hosted in.
- **Notebooks support:** We are data scientists, and can't help to open up a notebook and do some quick tests or early prototyping. This repo structure along with poetry allow for the virtual environment to be used as a jupyter kernel.
- **Code linting and formatting:** We use [ruff](https://docs.astral.sh/ruff/), a fast rust-based linter and formatter. Running basic code validations like formatting and linting might seem like a nuisance at first, but specially when collaborating in a team, having this done automatically saves on time for PR reviews, and removes personal preferences like "I format this way", letting people focus on the important things.
- **Tests**: Basic testing framework to get you started with setting up tests for your code. Testing isn't a really strong quality of Data Science projects, but we believe at least a couple of tests should be implemented.
- **GitHub config:** A minimal implementation of GitHub specific items, we include a PR template and a PR validation GitHub action which runs tests, linting and formatting.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10 or higher
- [Python poetry](https://python-poetry.org/)

# Usage

In order to get started with this template you can:
- Create a new repo from this template (recommended)
- Clone this repo

## Getting started

Once you have your copy of this template, you can simply run the following command to install the project:

```sh
poetry install
```

This takes care of installing the defined dependencies, this template has only dev dependencies, and [polars](https://pola.rs) as a project dependency.

### Using other python versions

This template is configured to use python 3.10 or above, by default poetry will create a virtual environment with the core python version available in your system. If you have another python version installed, you can specify it when creating the virtual environment:

```sh
# example for using python 3.11
poetry env use python3.11
```

If you want to use an older version you need to change the python version in the `pyproject.toml` file, and run the following command to recreate the virtual environment:

```sh
# example for using python 3.9
poetry env use python3.9
```

### Add more dependencies

It's very simple to use poetry to add more dependencies to your project, you can use the following command to add a new dependency:

```sh
poetry add <package-name>
```

If you want to add a development dependency, you can specify it using the `--group dev` option:

```sh
poetry add --group dev <package-name>
```

### Other poetry commands

Poetry has a lot of commands to help you manage your project, perhaps the most important one for our purposes is the `poetry run` command, which allows you to run scripts or commands in the context of the virtual environment:

```sh
poetry run <command>
```

For example, to run a python script you can use the following command:

```sh
poetry run python my_script.py
```

For more information on poetry commands you can check [poetry's official documentation](https://python-poetry.org/docs).

### Running tests

This template includes a basic test suite using `pytest`, you can run the tests using the following command:

```sh
poetry run pytest -v
```

### Linting and formatting

This template uses `ruff` for linting and formatting, you can run the following command to check for linting errors:

```sh
poetry run ruff check
```

And to format the code you can run:

```sh
poetry run ruff format
```

## The `src` directory

## Using jupyter notebooks

One of the dev dependencies installed is `ipykernel`, which allows you to use the virtual environment as a jupyter kernel. We recommend using VS Code's jupyter notebook support, since it atuomatically detects the virtual environment and uses it as a kernel. If you use this option, no further configuration is needed.

If you're setup requires for the use of the jupyter lab or notebook interface without exception, you can run the following command to install the kernel:

```sh
poetry run python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"
```

Change `myenv` to the name you want to give to the kernel, and `Python (myenv)` to the display name you want to show in the jupyter interface.

### On committing notebooks

We recommend not committing notebooks to the repository, since they can be quite large and make PR reviews difficult. If you need to commit a notebook, we recommend removing the output cells before committing. Additionally, the pr-validation action will fail if a notebook with executed cells is committed.

You can clear the output of cells in the notebooks UI or run the following command to clear all outputs from a notebook:

```sh
poetry run jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebooks/some_notebook.ipynb
```

## Documentation with mkdocs

This template uses `mkdocs` to generate documentation for the project. You can run the following command to start the development server:

```sh
poetry run mkdocs serve
```

This will start a development server that will automatically reload when changes are made to the documentation files. You can access the documentation by going to `http://localhost:8000` in your browser. For more information on how to use `mkdocs` you can check the [official documentation](https://www.mkdocs.org/getting-started).

## The PR Validation GitHub Action

This template includes a GitHub action that runs tests, linting and formatting on every PR. This is a good practice to ensure that the code is in good shape before merging it into the main branch, and to make reviews simpler since the code follows the same formatting diffs tend to be more focused on actual changes. The action is defined in the `.github/workflows/pr-validation.yml` file, and it runs on every PR to the main branch.
