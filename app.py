from fastapi import FastAPI, Query
from typing import Dict

from wikipedia_traversal import traverse_articles
from text_processing import build_word_frequency, filter_keywords
from models import KeywordsRequest

app = FastAPI(title="Wikipedia Word Frequency API")


@app.get("/word-frequency")
def get_word_frequency(
    article: str = Query(..., description="Wikipedia article title, e.g. 'Python (programming language)'"),
    depth: int = Query(0, ge=0, le=3, description="Depth of traversal (0 = only this article)")
) -> Dict[str, Dict[str, float]]:
    """
    Return a word-frequency dictionary for the given article and its linked articles up to `depth`.
    """
    text = traverse_articles(article, depth)
    return build_word_frequency(text)


@app.post("/keywords")
def post_keywords(req: KeywordsRequest) -> Dict[str, Dict[str, float]]:
    """
    Return filtered word-frequency dictionary based on ignore list and percentile threshold.
    """
    text = traverse_articles(req.article, req.depth)
    freq = build_word_frequency(text)
    return filter_keywords(freq, req.ignore_list, req.percentile)
