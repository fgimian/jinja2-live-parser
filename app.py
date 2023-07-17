#!/usr/bin/env python3
from flask import Flask, request, current_app
import jinja2
import ansible.plugins.filter.core
import ansible.plugins.filter.encryption
import ansible.plugins.filter.mathstuff
import ansible.plugins.filter.urls
import ansible.plugins.filter.urlsplit
import yaml


app = Flask(__name__)


@app.route("/")
def home():
    return current_app.send_static_file("index.html")


@app.post("/render")
def render_template():
    template = request.values.get("template", "")
    values = request.values.get("values", "")
    use_ansible_filters = bool(request.values.get("use_ansible_filters", 1, type=int))
    trim_blocks = bool(request.values.get("trim_blocks", 1, type=int))
    lstrip_blocks = bool(request.values.get("lstrip_blocks", 1, type=int))

    try:
        values = yaml.safe_load(values)
    except Exception as e:
        return "Error: values need to be in YAML format.\n{}".format(e)
    values = values or {}

    environment = jinja2.Environment(trim_blocks=trim_blocks, lstrip_blocks=lstrip_blocks)
    if use_ansible_filters:
        core_filters = ansible.plugins.filter.core.FilterModule()
        encryption_filters = ansible.plugins.filter.encryption.FilterModule()
        mathstuff_filters = ansible.plugins.filter.mathstuff.FilterModule()
        urls_filters = ansible.plugins.filter.urls.FilterModule()
        urlsplit_filters = ansible.plugins.filter.urlsplit.FilterModule()

        environment.filters.update(**core_filters.filters())
        environment.filters.update(**encryption_filters.filters())
        environment.filters.update(**mathstuff_filters.filters())
        environment.filters.update(**urls_filters.filters())
        environment.filters.update(**urlsplit_filters.filters())

    try:
        jinja_template = environment.from_string(template)
    except Exception as e:
        return "Error: unable to construct template.\n{}".format(e)

    try:
        return jinja_template.render(**values)
    except Exception as e:
        return "Error: template rendering failed.\n{}".format(e)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
