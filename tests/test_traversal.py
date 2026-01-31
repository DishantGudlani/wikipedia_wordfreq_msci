from unittest.mock import patch

from wikipedia_traversal import traverse_articles

MOCK_HTML_MAIN = """
<div id="bodyContent">
    <p>This is a test article about Python programming.</p>
    <a href="/wiki/Linked_Page">Linked Page</a>
</div>
"""

MOCK_HTML_LINKED = """
<div id="bodyContent">
    <p>This is the linked page with some extra content.</p>
</div>
"""


def fake_fetch_article_html(title: str) -> str:
    if title == "Python":
        return MOCK_HTML_MAIN
    if title == "Linked Page":
        return MOCK_HTML_LINKED
    return "<div id='bodyContent'><p>Empty page.</p></div>"


@patch("wikipedia_traversal.fetch_article_html", side_effect=fake_fetch_article_html)
def test_traverse_depth_zero(mock_fetch):
    text = traverse_articles("Python", max_depth=0)
    assert "Python programming" in text
    assert "linked page" not in text.lower()


@patch("wikipedia_traversal.fetch_article_html", side_effect=fake_fetch_article_html)
def test_traverse_depth_one(mock_fetch):
    text = traverse_articles("Python", max_depth=1)
    assert "Python programming" in text
    assert "linked page" in text.lower()
