# Jinja2 Live Parser (with Ansible Support)

Live parser for Jinja is a little web application that renders a Jinja2 template using the values specified in YAML format. The result is updated dynamically as you type.

This version is updated with the following changes:

- Dark theme and simplified design
- Ability to enable all Ansible Jinja2 filters
- Ability to toggle `trim_blocks` and `lstrip_blocks`
- Simplification of solution so you can run the entire app with Flask

The application is intended as a learning tool for those writing Jinja2 templates as part of their Ansible codebase.

Here's a screenshot of the app in action:

![Jnija2 Live Parser Screenshot](https://raw.githubusercontent.com/fgimian/jinja2-live-parser/master/images/screenshot.png)

See the official [Jinja website](http://jinja.pocoo.org/) and [Ansible website](https://www.ansible.com/) to learn more about the respective tools.

**Note**: This application will only run on Linux due to the use of Ansible which is not supported on other operating systems.

## Quick Start

Install [Python](https://www.python.org/) and [Poetry](https://python-poetry.org/) and run the following:

```bash
# Install dependencies.
poetry install

# Run the application.
poetry run python3 app.py
```

## Original Motivation

At the time writing this implementation, a running live parser for Jinja was not readily available online. [This StackOverflow answer](https://stackoverflow.com/questions/20145709/looking-for-a-jinja-online-or-at-least-live-parser/25852297#25852297) provides a working solution which is further developed here.

The improvements made include dynamic updating of the rendered output as the user types. The improved solution is reported as [another answer](https://stackoverflow.com/a/48907913/9391289) to the same question on StackOverflow.
