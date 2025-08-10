import re

patterns = {
    "APA": re.compile(
        r"^[A-Z][a-z]+,\s*(?:[A-Z]\.\s*)+(?:,\s*(?:&|and)\s*[A-Z][a-z]+,\s*(?:[A-Z]\.\s*)+)*\s*\(\d{4}\)",
        re.IGNORECASE
    ),
    "MLA": re.compile(
        r"^[A-Z][a-z]+,\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\.\s+\"[^\"]+\"",
        re.IGNORECASE
    ),
    "Chicago": re.compile(
        r"^[A-Z][a-z]+,\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\.\s*\(\d{4}\)",
        re.IGNORECASE
    ),
    "IEEE": re.compile(
        r"^\[\d+\]\s+(?:[A-Z]\.\s*)+[A-Z][a-z]+,\s+\"[^\"]+\"",
        re.IGNORECASE
    )
}
