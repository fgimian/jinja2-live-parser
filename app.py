import ansible.plugins.filter.core
import ansible.plugins.filter.encryption
import ansible.plugins.filter.mathstuff
import ansible.plugins.filter.urls
import ansible.plugins.filter.urlsplit
import jinja2
import yaml
from flask import Flask, Response, current_app, request

app = Flask(__name__)


@app.route("/")
def home() -> Response:
    return current_app.send_static_file("index.html")


@app.post("/render")
def render_template() -> Response:
    template = request.values.get("template", "")
    values = request.values.get("values", "")
    use_ansible_filters = bool(request.values.get("use_ansible_filters", 1, type=int))
    trim_blocks = bool(request.values.get("trim_blocks", 1, type=int))
    lstrip_blocks = bool(request.values.get("lstrip_blocks", 1, type=int))

    try:
        values = yaml.safe_load(values)
    except yaml.YAMLError as e:
        return f"Error: values need to be in YAML format.\n{e}"
    values = values or {}

    environment = jinja2.Environment(
        autoescape=True,
        trim_blocks=trim_blocks,
        lstrip_blocks=lstrip_blocks,
        extensions=[
            "jinja2.ext.i18n",
            "jinja2.ext.do",
            "jinja2.ext.loopcontrols",
            "jinja2.ext.debug",
        ],
    )
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
    except jinja2.exceptions.TemplateSyntaxError as e:
        return f"Error: unable to construct template.\n{e}"

    return jinja_template.render(**values)
