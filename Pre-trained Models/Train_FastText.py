import fasttext

target_path = "E:\\TFM\\Biomedical Spanish Corpus\\Final_Corpus\\Spanish_Biomedical_Corpus_Processed.txt"

# Skipgram model
model = fasttext.skipgram(target_path,
                          'Biomedical_Spanish_FastText_10epoch',
                          dim=300,
                          epoch=10,
                          min_count=20,
                          neg=20,
                          t=6e-5,
                          thread=7,
                          encoding='utf8',
                          )

print(model.words)  # list of words in dictionary