import string
# import nltk
from nltk import word_tokenize


def split(data: str) -> list:
    text = "".join([ch for ch in data if ch not in string.punctuation])
    text = "".join([ch for ch in data if ch not in string.digits])
    text_tokens = word_tokenize(text)
    return text_tokens



