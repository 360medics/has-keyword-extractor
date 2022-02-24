# HAS Keyword Extractor (not only for HAS, universal and multilingual)
[![Generic badge](https://img.shields.io/badge/python-3.8-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/python-3.9-green.svg)](https://shields.io/)

to install the package : 
```bash
pip install git+https://github.com/360medics/has-keyword-extractor.git@master
```


to execute the code inside your code :
```python
from has_keyword_extractor._runner import st_process_multiple_doc
import spacy
import json
nlp = spacy.load("fr_core_news_sm")
file = json.load(open('./data/test.json', 'r'))
keywords = st_process_multiple_doc(file, nlp, 0.01, 0.5)
```

to execute the application into the console
```shell
extract_keywords process-docs --alpha 0.04 --threshold 0.5 --path ./data/processed-HAS.json --spacy-model fr_core_news_sm
```

You can find more information about this algorithm in this notebook : `notebooks/statistic-keyword-extraction.ipynb`.

The other notebook is another algorithm that you can implement for fun : `notebooks/statistic-keyword-extraction.ipynb`.
My idea was to find a way to combine these both methods

## TODO
* test with tools to get keywords


