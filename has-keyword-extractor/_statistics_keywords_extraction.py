from collections import Counter
from typing import Dict

import nltk

from compute_cumulative_frequencies import (
    compute_cumul_freq_monogram,
    compute_cumul_freq_bigram,
)
from fbi import compute_fbi
from fni import compute_fni
from hwo import compute_hwo
from hwpo import compute_hwpo
from ranked_ngrams import compute_ranked_ngrams


class StatisticsKeywordsExtraction:
    def __init__(self, words: list[str], alpha: float, threshold: float):
        self.words = words
        self.bigram_frequencies = Counter(i for i in list(nltk.bigrams(words)))
        self.monogram_frequencies = Counter(words)
        self.alpha = alpha
        self.threshold = threshold

    def extract_keywords(self) -> Dict:
        cumul_monogram = compute_cumul_freq_monogram(self.monogram_frequencies)
        cumul_bigram = compute_cumul_freq_bigram(self.bigram_frequencies)

        hwo_bow = {
            word: compute_hwo(word, self.monogram_frequencies, cumul_monogram)
            for word in self.words
        }

        hwpo_bow = {
            bigram: compute_hwpo(bigram, self.bigram_frequencies, cumul_bigram)
            for bigram in list(self.bigram_frequencies)
        }

        fbi_bigrams = compute_fbi(
            self.bigram_frequencies, hwpo_bow, hwo_bow, self.alpha, self.threshold
        )

        fni_ngrams = compute_fni(fbi_bigrams.items())

        return compute_ranked_ngrams(fni_ngrams, self.bigram_frequencies, self.monogram_frequencies)
