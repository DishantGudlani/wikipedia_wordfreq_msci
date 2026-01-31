from collections import deque
from typing import List, Set, Tuple

import requests
from bs4 import BeautifulSoup

WIKI_BASE_URL = "https://en.wikipedia.org/wiki/"


def fetch_article_html(title: str) -> str:
    """
    Fetch raw HTML for a given Wikipedia article title.
    """
    url = WIKI_BASE_URL + title.replace(" ", "_")
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.text


def extract_text_and_links(html: str) -> Tuple[str, List[str]]:
    """
    Extract visible text and internal article links from a Wikipedia page.
    """
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find("div", {"id": "bodyContent"}) or soup

    text = content.get_text(separator=" ", strip=True)

    links: List[str] = []
    for a in content.find_all("a", href=True):
        href = a["href"]
        # Only follow normal article links, skip special pages like "File:", "Help:", etc.
        if href.startswith("/wiki/") and ":" not in href:
            title = href[len("/wiki/"):].replace("_", " ")
            links.append(title)

    return text, links


def traverse_articles(start_title: str, max_depth: int) -> str:
    """
    Breadth-first traversal of Wikipedia articles starting from `start_title`.

    Collects text from the starting article and its linked articles up to `max_depth`.
    """
    visited: Set[str] = set()
    queue = deque([(start_title, 0)])
    collected_text: List[str] = []

    while queue:
        title, depth = queue.popleft()

        if title in visited or depth > max_depth:
            continue

        visited.add(title)

        try:
            html = fetch_article_html(title)
        except requests.RequestException:
            # If a page fails to load, just skip it and move on.
            continue

        text, links = extract_text_and_links(html)
        collected_text.append(text)

        if depth < max_depth:
            for link_title in links:
                if link_title not in visited:
                    queue.append((link_title, depth + 1))

    return " ".join(collected_text)
