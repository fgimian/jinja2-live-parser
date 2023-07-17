# Jinja2 Live Parser (with Ansible Support)

Live parser for Jinja is a web application which fills a template with values specified in YAML format. The resulting rendering is updated dynamically as the user types.

This version is updated with the following changes:

- Dark theme
- Ability to enable all Ansible Jinja2 filters
- Ability to toggle `trim_blocks` and `lstrip_blocks`
- Simplification of solution so you can run the entire app with Flask

For more information about Jinja visit the official website at [http://jinja.pocoo.org/](http://jinja.pocoo.org/).

## Installation

Install [Poetry](https://python-poetry.org/) and run the following:

```bash
# Install dependencies.
poetry install

# Run the application.
python3 app.py
```

## Motivation

At the time writing this implementation, a running live parser for Jinja was not readily available online. [This StackOverflow answer](https://stackoverflow.com/questions/20145709/looking-for-a-jinja-online-or-at-least-live-parser/25852297#25852297) provides a working solution which is further developed here. The improvements include dynamic update of result as the user types and nginx server serving static files and acting as a reverse proxy. This solution is reported as [another answer](https://stackoverflow.com/a/48907913/9391289) to the same question on StackOverflow.
