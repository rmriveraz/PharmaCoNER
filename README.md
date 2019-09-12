# Embeddings
This repository contains the word embeddings generated from biomedical Spanish texts corpora.

# Corpus detail

The corpus was gathered from Spanish biomedical texts from different multilingual biomedicalsources:

  - IBECS (Spanish Bibliographical Index in Health Sciences): corpus that collects scientific journals covering multiple fields in health sciences. Contains titles and abstracts from 168,198 records in English and Spanish.
  - SciELO (Scientific Electronic Library Online): corpus gathers electronic publications of complete full text articles from scientific journals of Latin America, South Africa and Spain. Contains titles and abstracts from 161,710 records in English and Spanish.
  - Pubmed: free search engine used to accessthe MedlineNLM (https://www.ncbi.nlm.nih.gov/pubmed/). Contains titles and abstracts from 127,619 records.
  - MedlinePlus: corpus with health topics, drugs and supplements, laboratory test information and medical encyclopedia texts contains 7,033 articles in English and Spanish.
  - UFAL Medical Corpus: is a collection of parallel corpora of medicaland general domain texts.
  
All corpus data files can be found in the next link: http://temu.bsc.es/mespen/

# Pre-trained Models

  # FastText

  We  used  the  FastText  (Bojanowski  et  al.,  2016) implementation to train our word embeddings using  the preprocesed Spanish  Biomedical  corpus (FastText-SBC). Moreover, we trained a concept embedding model replacing biomedical concepts  in  the  Spanish  Biomedical  corpus  withtheir unique SNOMED-CT Spanish Edition iden-tifier  (SNOMED-SBC).  We  used  the  PyMedTer-mino library (Lamy et al., 2015) for concept indexing using full-text search and fuzzy search with threshold.

  # Train Parameters

    - Dimension = 300
    - epoch=10,20
    - min_count=20
    - neg=20
    - t=6e-5
    - thread=7
    - encoding='utf8'
    - min subword-ngram = 3
    - max subword-ngram = 6

  # Links to the embeddings

    - FastText-SBC 
    - SNOMED-SBC
