"""Tools for text preprocessing."""
import re

import demoji


def text_preprocessing(text: str) -> str:
    """Drop trash symbols from text

    @param text: raw text
    @return: clean text
    """
    text = re.sub(r"<[^>]*>", " ", text)
    text = re.sub(r"^\[id\d*|.*\],*\s*", "", text)
    text = re.sub(r"(&quot;)|(&lt;)|(&gt;)|(&amp;)|(&apos;)", " ", text)
    text = re.sub(r"https?://(www\.)?[-a-zA-Z0-9@:%._+~#=]{2,256}\."
                  r"[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&/=]*)"," ", text)
    text = re.sub(r"\[[^\[\]]+\|([^\[\]]+)\]", r"\1", text)
    text = re.sub(r"(&#\d+;)", " ", text)
    text = re.sub(r"[(_#*=^/`@«»©…“•—<>\[\]\"'+%|&]", " ", text)
    text = re.sub(r"[\;:)(_#*=^/`@«»©…“•—<>\[\]\"'+%|&]", " ", text)
    text = text.replace("  ", " ")
    text = text.replace("--", " ")
    text = text.replace('\n', ' ')
    text = re.sub("\s\s+", " ", text)
    text = demoji.replace(text, "")
    return text.strip()
