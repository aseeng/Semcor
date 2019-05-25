from nltk.corpus import semcor
import utils

count = 0
num_sentences = 0
for i in range(100):
    sent = semcor.xml('brown2/tagfiles/br-n12.xml').findall('context/p/s')[i]

    sentence = ""
    name = ""

    for wordform in sent.getchildren():
        sentence += wordform.text + " "
        if wordform.get('pos') == "NN" and wordform.text != "anyone":
            name = wordform.text
            sense_key = wordform.get('lexsn')

    context = utils.tokenize(sentence)

    if name is not "":
        best_sense = utils.find_synset(context,name)
        num_sentences += 1
        if sense_key == best_sense.lemmas()[0].key()[-9:]:
            count += 1
    if num_sentences == 50:
        break

print("accuracy = " + str(count*100/num_sentences) + " %")