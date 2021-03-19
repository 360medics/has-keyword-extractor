# HAS Keyword Extractor
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

[![Generic badge](https://img.shields.io/badge/python-3.8-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/python-3.9-green.svg)](https://shields.io/)