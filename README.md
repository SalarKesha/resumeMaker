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
            "title": "Github",
            "url": "https://github.com/SalarKesha",
            "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg",
        },
        {
            "title": "Linkedin",
            "url": "https://www.linkedin.com/in/salar-keshavarzi/",
            "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg",
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
    "skills": [
        {
            "name": "...",
            "icon": "...",
        }
    ],
}

LANGS = {"en": en_context}
```

Each contact link can include an `icon` URL. Omit `icon` or set it to `None`
to show the link title without an icon.

3 - Render templates
```shell
poetry run python main.py
```

Open `output/resume_en.html` in a browser. The generated resume uses local,
compiled Tailwind CSS and the bundled Inter font. Node.js is only needed when
changing the design; the existing Python generation command still works by itself.
Skill icons with remote URLs require an internet connection.

### Customize the design with Tailwind

Install Node.js 20 or newer, then install the styling tools:

```shell
npm ci
```

Edit utility classes in `templates/template.html`. Theme and font settings live
in `static/tailwind.css`. Rebuild the stylesheet after making changes:

```shell
npm run build:css
poetry run python main.py
```

During development, `npm run watch:css` rebuilds styles automatically. Rerun the
Python command after changing the template to update the generated HTML. Commit
the generated `static/style.css` alongside template changes so resumes can be
generated without Node.js or a CDN. The build follows the
[Tailwind CLI workflow](https://tailwindcss.com/docs/installation/tailwind-cli).

The layout stacks on small screens and supports the existing `lang` and `dir`
context values, including RTL. To export a PDF, use your browser's **Print → Save
as PDF** with A4 paper and browser headers and footers disabled. Print styles
remove the screen frame, use a compact two-column layout, and keep individual
experience and education entries together where possible. Longer resumes can
span multiple pages.

