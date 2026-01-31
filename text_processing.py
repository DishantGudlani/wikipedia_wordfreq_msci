import re
from collections import Counter
from typing import Dict, List

WORD_PATTERN = re.compile(r"[a-zA-Z]+")


def tokenize(text: str) -> List[str]:
    """
    Very simple tokenizer: lowercase and keep only alphabetic sequences.
    """
    text = text.lower()
    return WORD_PATTERN.findall(text)


def build_word_frequency(text: str) -> Dict[str, Dict[str, float]]:
    """
    Build a dictionary: word -> {count, percentage}.
    """
    tokens = tokenize(text)
    total = len(tokens)
    counts = Counter(tokens)

    result: Dict[str, Dict[str, float]] = {}
    if total == 0:
        return result

    for word, count in counts.items():
        result[word] = {
            "count": count,
            "percentage": (count / total) * 100.0,
        }

    return result


def filter_keywords(
    freq_dict: Dict[str, Dict[str, float]],
    ignore_list: List[str],
    percentile: int,
) -> Dict[str, Dict[str, float]]:
    """
    Filter out ignored words and keep only words whose count is at or above
    the given percentile threshold.
    """
    ignore_set = {w.lower() for w in ignore_list}
    filtered = {w: v for w, v in freq_dict.items() if w not in ignore_set}

    if not filtered:
        return {}

    counts = sorted(v["count"] for v in filtered.values())
    # Simple percentile calculation: pick index based on percentile
    idx = int(len(counts) * (percentile / 100))
    if idx >= len(counts):
        idx = len(counts) - 1
    threshold = counts[idx]

    return {w: v for w, v in filtered.items() if v["count"] >= threshold}
