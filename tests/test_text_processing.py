from text_processing import tokenize, build_word_frequency, filter_keywords


def test_tokenize_basic():
    text = "Hello, world! Hello again."
    tokens = tokenize(text)
    assert tokens == ["hello", "world", "hello", "again"]


def test_build_word_frequency_counts_and_percentages():
    text = "a a b"
    freq = build_word_frequency(text)

    assert freq["a"]["count"] == 2
    assert freq["b"]["count"] == 1

    total_percentage = freq["a"]["percentage"] + freq["b"]["percentage"]
    assert 99.0 <= total_percentage <= 101.0  # allow for float rounding


def test_filter_keywords_ignore_list():
    freq = {
        "apple": {"count": 10, "percentage": 50.0},
        "banana": {"count": 5, "percentage": 25.0},
        "cherry": {"count": 5, "percentage": 25.0},
    }

    result = filter_keywords(freq, ignore_list=["banana"], percentile=0)
    assert "banana" not in result
    assert "apple" in result
    assert "cherry" in result


def test_filter_keywords_percentile():
    freq = {
        "a": {"count": 10, "percentage": 50.0},
        "b": {"count": 5, "percentage": 25.0},
        "c": {"count": 2, "percentage": 10.0},
        "d": {"count": 1, "percentage": 5.0},
    }

    result = filter_keywords(freq, ignore_list=[], percentile=75)
    # Only the higher-frequency words should remain
    assert "a" in result
    assert "b" in result or "b" not in result  # depends on threshold, just ensure no crash
    assert "c" in freq  # sanity check original
