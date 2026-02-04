from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader

NAV = [
    ("Online-Seminar-Series", "Online Seminar Series"),
    ("Previous-Seminars", "Previous Seminars"),
]

CONTENT_DIR = Path("content")
OUTPUT_DIR = Path("output")
TEMPLATE_DIR = Path("templates")

OUTPUT_DIR.mkdir(exist_ok=True)

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template("page.html")

for md_file in CONTENT_DIR.glob("*.md"):
    md_text = md_file.read_text(encoding="utf-8")
    html_content = markdown.markdown(md_text, extensions=["extra"])

    rendered = template.render(
        title=md_file.stem,
        nav=NAV,
        page_name=md_file.stem,   # 🔑 wichtig für .active
        content=html_content,
        lang="en"
    )

    out_file = OUTPUT_DIR / f"{md_file.stem}.html"
    out_file.write_text(rendered, encoding="utf-8")

print("Website build finished!")
