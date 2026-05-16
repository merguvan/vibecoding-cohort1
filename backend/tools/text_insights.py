import re


def text_insights(text: str) -> str:
    """Return simple statistics about a text."""
    clean_text = text.strip()
    words = re.findall(r"\b[\w'-]+\b", clean_text)
    sentences = [s for s in re.split(r"[.!?]+", clean_text) if s.strip()]
    reading_minutes = max(1, round(len(words) / 200)) if words else 0

    return (
        "Metin analizi:\n"
        f"- Kelime sayisi: {len(words)}\n"
        f"- Karakter sayisi: {len(clean_text)}\n"
        f"- Cumle sayisi: {len(sentences)}\n"
        f"- Tahmini okuma suresi: {reading_minutes} dakika"
    )
