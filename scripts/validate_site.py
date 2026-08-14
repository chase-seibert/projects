#!/usr/bin/env python3
"""Validate the dependency-free static portfolio."""

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.local_references: list[str] = []
        self.project_cards = 0
        self.scripts = 0
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "article" and "project-card" in classes:
            self.project_cards += 1
        if tag == "script":
            self.scripts += 1
        for attribute in ("href", "src"):
            value = values.get(attribute)
            if value and not value.startswith(("#", "http://", "https://", "mailto:")):
                self.local_references.append(value)

    def handle_data(self, data: str) -> None:
        self.text.append(data)


def main() -> None:
    index = SITE / "index.html"
    assert index.is_file(), "site/index.html is missing"
    assert (SITE / "styles.css").is_file(), "site/styles.css is missing"

    parser = SiteParser()
    parser.feed(index.read_text(encoding="utf-8"))

    assert parser.scripts == 0, "The static page must not include JavaScript"
    assert parser.project_cards == 12, f"Expected 12 project cards, found {parser.project_cards}"

    page_text = " ".join(parser.text)
    for project in (
        "Cookbook",
        "Sideline Save",
        "Chase Seibert Blog",
        "Chase Sidekick",
        "Calorie Tracker",
        "Miclog Desktop",
        "Remote Agent",
        "Clipboard Markup",
        "ICS Combine",
        "CronTab Manager",
        "RSS Combine",
    ):
        assert project in page_text, f"Missing project: {project}"

    for reference in parser.local_references:
        path = (SITE / reference).resolve()
        assert SITE.resolve() in path.parents or path == SITE.resolve(), f"Reference escapes site: {reference}"
        assert path.is_file(), f"Missing local asset: {reference}"

    print(f"Static site is valid: {parser.project_cards} projects, no JavaScript, all assets present.")


if __name__ == "__main__":
    main()
