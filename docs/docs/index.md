# PhiQus Starter DS Project Repo

Project documentation using [mkdocs.org](https://www.mkdocs.org) with the [material theme](https://squidfunk.github.io/mkdocs-material). This is the index page for all documentation generated.

## Dev Server

It's quite simple to work locally with mkdocs to visualize the compiled html with autoreload. To enable the development server for the docs simply run these commands:

```bash
# make sure you're on the root docs directory
cd docs

# run the server with poetry
poetry run mkdocs serve
```

## Suggested Docs Layout

We suggest the following structure for your documentation:

```
mkdocs.yml       # (NOT OPTIONAL) The configuration file
docs/
  index.md       # The documentation homepage (this page)
  quickstart.md  # A page for getting started with the project
  ...            # Other markdown pages, images and other files
  reference/     # Directory for all autodocumentation
    index.md     # Index page for the reference section of docs
    deleteme.md  # Example deleteme module in this template
    ...          # Other autodoc pages
```

You can add or remove pages and sections, this layout is only a suggestion. However, we do heavily recommend keeping all autodocumented code in its dedicated section.
