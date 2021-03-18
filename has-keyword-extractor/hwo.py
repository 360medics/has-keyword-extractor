from typing import Dict


def compute_hwo(word: str, monogram_frequency: Dict, cumul_monogram: Dict):
    key_max = max(list(cumul_monogram.keys()))
    return cumul_monogram[monogram_frequency[word]] / cumul_monogram[key_max]
