# Resume Maker
### Multi langs resume generator using Jinja2

1 - Install dependencies
```shell
poetry install
```

2 - Edit variables.py
```python
sample_context : Context = ...
LANGS = {"lang": sample_context}
```

3 - Render templates
```shell
poetry run python run.py
```