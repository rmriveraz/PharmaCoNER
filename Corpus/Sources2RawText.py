import glob
import os
import chardet
import codecs
import csv
import re
import ftfy
from bs4 import BeautifulSoup
import time
from tqdm import *


def fixMojibake(text):
    correct_str = text
    falsely_decoded_str = text
    encoded_str = None

    try:
        encoded_str = falsely_decoded_str.encode("cp850")
    except UnicodeEncodeError:
        print("could not encode falsely decoded string")
        pass

    if encoded_str is not None and encoded_str:
        detected_encoding = chardet.detect(encoded_str)["encoding"]

        try:
            correct_str = encoded_str.decode(detected_encoding)
        except UnicodeEncodeError:
            print("could not decode encoded_str as %s" % detected_encoding)
            pass

        with codecs.open("output.txt", "w", "utf-8-sig") as out:
            return correct_str

    return correct_str


pathIBECS = "E:\\TFM\\Biomedical Spanish Corpus\\dublin_core\\"
pathSCIELO = "E:\\TFM\\Biomedical Spanish Corpus\\dublin_core_extended\\"
pathPUBMED = "E:\\TFM\\Biomedical Spanish Corpus\\PubMed\\dublin_core\\"
pathMEDLINE = "E:\\TFM\\Biomedical Spanish Corpus\\health_topics_DC\\"
pathMEDLINE_TEXT = "E:\\TFM\\Biomedical Spanish Corpus\\TEI_ES\\"
pathUFAL = "E:\\TFM\\Biomedical Spanish Corpus\\UFAL_Medical_Corpus1.0_for_WMT17\\UFAL_medical_shuffled\\"
targetPath = "E:\\TFM\\Biomedical Spanish Corpus\\"

text = ""

# regex = re.compile("[^A-Za-z0-9\|[ :\]'.óáéíúñ\-\nçã?¿¡@#~%\$/()=!«»,;&…®êüöºªβõ*+è“”´≤<>_]+")


# leer xml
for root, dirs, files in os.walk(pathIBECS):
   for file in glob.glob(os.path.join(root, '*.xml')):
        fileinput = open(file, "r", encoding="utf8")
        print("Archivo: "+file)
        for line in fileinput:
#            line = fixMojibake(line)
            line = line.replace("dc:description","description")
            line = line.replace("dc:title","title")
            soup = BeautifulSoup(line)
            for xmlText in soup.findAll('title'):
                text += xmlText.text + "\n"
            for xmlText in soup.findAll('description'):
                text += xmlText.text+"\n"

with open(targetPath + "\\Spanish_Biomedical_Corpus.txt", 'a+', encoding="utf8") as txtFile:
    txtFile.write(text)

# leer xml
for root, dirs, files in os.walk(pathSCIELO):
   for file in glob.glob(os.path.join(root, '*.xml')):
        fileinput = open(file, "r", encoding="utf8")
        print("Archivo: "+file)
        for line in fileinput:
#            line = fixMojibake(line)
            line = line.replace("dc:description","description")
            line = line.replace("dc:title","title")
            soup = BeautifulSoup(line)
            for xmlText in soup.findAll('title'):
                text += xmlText.text + "\n"
            for xmlText in soup.findAll('description'):
                text += xmlText.text+"\n"

with open(targetPath + "\\Spanish_Biomedical_Corpus.txt", 'a+', encoding="utf8") as txtFile:
    txtFile.write(text)


# leer xml
for root, dirs, files in os.walk(pathPUBMED):
   for file in glob.glob(os.path.join(root, '*.xml')):
        fileinput = open(file, "r", encoding="utf8")
        print("Archivo: "+file)
        for line in fileinput:
#            line = fixMojibake(line)
            line = line.replace("dc:description","description")
            line = line.replace("dc:title","title")
            soup = BeautifulSoup(line)
            for xmlText in soup.findAll('title'):
                text += xmlText.text + "\n"
            for xmlText in soup.findAll('description'):
                text += xmlText.text+"\n"

with open(targetPath + "\\Spanish_Biomedical_Corpus.txt", 'a+', encoding="utf8") as txtFile:
    txtFile.write(text)


# leer txt
for root, dirs, files in os.walk(pathMEDLINE_TEXT):
    for file in glob.glob(os.path.join(root, '*.txt')):
        text = ""
        fileinput = open(file, "r", encoding="utf8")
        for line in fileinput:
            # if regex.search(line.lower()) is not None:
            #     print(regex.search(line))
            #     line = fixMojibake(line)
            text += line

        with open(targetPath + "\\Spanish_Biomedical_Corpus.txt", 'a+', encoding="utf8") as txtFile:
            txtFile.write(text)

with open(pathUFAL + "shuffled.es-en", "r", encoding='utf8') as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        if len(line) > 2 and 'medical_corpus' in line[2]:
            text += line[0]+"\n"

    with open(targetPath + "\\Spanish_Biomedical_Corpus.txt", 'a+', encoding="utf8") as txtFile:
        txtFile.write(text)
