from nltk import WordNetLemmatizer
import utils
import re

pathFile = 'sentences.txt'
lemmatizer = WordNetLemmatizer()

with open(pathFile) as file:
    for line in file:
        matchObj = re.match(".*\\*\\*(.*)\\*\\*", line, re.M | re.I)
        word = lemmatizer.lemmatize(matchObj.group(1).lower())
        line = line.replace("*","")
        context = utils.tokenize(line)
        best_sense = utils.find_synset(context, word)

        synonyms = best_sense.lemma_names()
        for synonym in synonyms:
            if synonym != word:
                newLine = line.replace(word, synonym)
                print(line + "   " + best_sense.definition() + "\n       " + newLine)
                break

        if len(synonyms) == 1:
            print(line + "   " + best_sense.definition() + "\n")