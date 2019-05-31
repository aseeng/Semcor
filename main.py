from nltk import WordNetLemmatizer
import utils
import re

pathFile = 'asset\sentences.txt'
lemmatizer = WordNetLemmatizer()

with open(pathFile) as file:
    for line in file:
        matchObj = re.match(".*\\*\\*(.*)\\*\\*", line, re.M | re.I)
        word = lemmatizer.lemmatize(matchObj.group(1).lower())
        line = line.replace("*","")
        context = utils.tokenize(line)
        best_sense = utils.find_synset(context, word)

        synonyms = best_sense.lemma_names()
        print(str(best_sense.offset()) + "    " + best_sense.definition())

        for synonym in synonyms:
            newLine = line.replace(word, synonym)
            print(newLine[:-1])

        print()