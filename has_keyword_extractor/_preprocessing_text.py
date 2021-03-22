import re
from nltk.corpus import stopwords


def preprocessing_text(text: str, nlp, sep="[PUNCT]") -> list:
    # tokenize text
    doc = nlp(text)
    # remove stopwords
    words_list = []
    text = (
        re.sub(r"\d+", "", text)
        .lower()
        .replace("\\n", "")
        .replace("\\t", "")
        .replace("\\xa", "")
        .replace("\n", "")
        .replace("'", "")
        .strip()
    )
    stopwords_custom = stopwords.words("french") + [
        "ci-dessous",
        "ci-dessus",
        "préalablement",
        "précédemment",
    ]
    for token in doc:
        if token.is_punct or token.is_stop or token.text in stopwords_custom:
            words_list.append(sep)
        elif not token.is_space:
            words_list.append(token.text)
    return words_list
