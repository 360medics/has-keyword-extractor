from typing import Dict

import spacy

from _statistics_keywords_extraction import StatisticsKeywordsExtraction
from preprocessing_text import preprocessing_text


def st_process_doc(text: str, nlp, alpha: float, threshold: float):
    return StatisticsKeywordsExtraction(
        preprocessing_text(text, nlp), alpha, threshold
    ).extract_keywords()


def st_process_multiple_doc(
    documents: Dict[str, str], spacy_model: str, alpha: float, threshold: float
):
    nlp = spacy.load(spacy_model)
    return {
        title: st_process_doc(content, nlp, alpha, threshold)
        for title, content in documents.items()
    }
