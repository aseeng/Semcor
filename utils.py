from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import string

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stemmatizer = PorterStemmer()


def getHyponyms(synset):
    hyponyms = set()
    for s in synset.hyponyms():
        for lemma in s.lemma_names():
            hyponyms = hyponyms.union(tokenize(lemma))
        hyponyms = hyponyms.union(tokenize(s.definition()))
    return hyponyms


def getExamples(synset):
    examples = set()
    for example in synset.examples():
        examples = examples.union(tokenize(example))

    return examples


def get_signature(synset):
    # si crea l'insieme signature
    signature = set()

    for lemma in synset.lemma_names():
        signature = signature.union(tokenize(lemma))

    # si aggiunge la definizione del synset
    signature = signature.union(tokenize(synset.definition()))

    # si aggiungono gli esempi
    signature = signature.union(getExamples(synset))

    # si aggiungono gli iponimi diretti
    signature = signature.union(getHyponyms(synset))

    return signature


def find_synset(context,word):
  #  trova il miglior synset della parola word nel contesto context.
    best_sense = wn.synsets(word)[0]
    max_overlap = 0

    for synset in wn.synsets(word):
        signature = get_signature(synset)
        overlap = len(signature & context)
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = synset

    return best_sense


def tokenize(sentence):
    tokens = set(word for word in word_tokenize(sentence.lower()) if word not in stop_words and word not in string.punctuation)

    for token in tokens:
        tokens = tokens.union(lemmatizer.lemmatize(token))
        tokens = tokens.union(stemmatizer.stem(token))

    tokens = tokens.difference(token for token in tokens if len(token)<2)
    return tokens
