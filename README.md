# Resume Maker
### Multi langs resume generator using Jinja2

1 - Install dependencies
```shell
poetry install
```

2 - Add variables.py
```python
from data_types import Context

en_context: Context = {
    "lang": "en",
    "dir": "ltr",
    "fullname": "...",
    "role": "...",
    "links": [
        {
            "title": "...",
            "url": "...",
        },
    ],
    "about": """...""",
    "experiences": [
        {
            "title": "...",
            "sub_title": "...",
            "role": "...",
            "description": """...""",
            "stack": "...",
            "domain": "...",
        }
    ],
    "educations": [
        {
            "field": "...",
            "location": "...",
            "degree": "...",
            "date": "...",
        }
    ],
    "hard_skills": [
        {"title": "...", "content": "..."},
    ],
    "soft_skills": [
        "...",
    ],
}

LANGS = {"en": en_context}
```

3 - Render templates
```shell
poetry run python run.py
```

