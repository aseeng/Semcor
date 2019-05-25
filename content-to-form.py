import utils

best = []
with open("definitions.txt", "r") as f:
    contexts = dict()
    index = 0
    for line in f:
        contexts[index] = utils.tokenize(line)
        index += 1

    best_synset = utils.get_best_sense(contexts)
    print(str(best_synset))
