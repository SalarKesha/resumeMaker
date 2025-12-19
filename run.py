from jinja2 import Environment, FileSystemLoader
from data_types import Context
import os
from variables import LANGS

env = Environment(loader=FileSystemLoader("./templates"))
template = env.get_template("template.html")


def render(output_name: str, context: Context):
    html = template.render(context)
    os.makedirs("output", exist_ok=True)
    with open(f"output/{output_name}", "w", encoding="utf-8") as f:
        f.write(html)


for key, value in LANGS.items():
    file_name = f"resume_{key}.html"
    render(file_name, value)

print("Resumes generated in /output")
