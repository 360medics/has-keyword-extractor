from typing import Dict

from alive_progress import alive_bar

from _statistics_keywords_extraction import StatisticsKeywordsExtraction
from _preprocessing_text import preprocessing_text


def st_process_doc(text: str, nlp, alpha: float, threshold: float):
    return StatisticsKeywordsExtraction(
        preprocessing_text(text, nlp), alpha, threshold
    ).extract_keywords()


def st_process_multiple_doc(
    documents: Dict[str, str], nlp, alpha: float, threshold: float
):
    print('🔎 Begin keyword extraction : ')
    result = {}
    with alive_bar(len(documents)) as progress_bar:
        for title, content in documents.items():
            result[title] = st_process_doc(content, nlp, alpha, threshold)
            progress_bar()
    print('keyword extraction is ended')
    return result
