import string
import spacy


nlp = spacy.load('es_core_news_md', disable=["parser", "tagger"])

final_text = ""

input_path = "E:\\TFM\\Biomedical Spanish Corpus\\Final_Corpus\\Spanish_Biomedical_Corpus.txt"
target_path = "E:\\TFM\\Biomedical Spanish Corpus\\Final_Corpus\\Spanish_Biomedical_Corpus_Processed.txt"

remove = dict.fromkeys(map(ord, string.punctuation))

with open(input_path,encoding='utf8') as inputfile:
   f = inputfile.read().translate(str.maketrans('', '', string.punctuation)).lower().strip()
   nlp.max_length = len(f)
   doc = nlp(f)

   for token in doc:
       final_text += token.lemma_ + " "

   with open(target_path, 'w+', encoding="utf8") as outputfile:
       outputfile.write(final_text)
       outputfile.close()
