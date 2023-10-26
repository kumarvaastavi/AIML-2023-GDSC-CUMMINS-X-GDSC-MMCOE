import nltk
import sys
import grammar as g
import re

# creating a grammer object to read from the string of grammer rules 
grammar = nltk.CFG.fromstring(g.NONTERMINALS + g.TERMINALS)

# creating a parser variable to save and parse the grammer
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    pattern = r'\b(?:[A-Za-z]+[0-9]*[A-Za-z]*[0-9]*)+\b'

    # Use re.sub to replace non-matching words with an empty string
    result = re.sub(pattern, '', sentence)
    for word in result:
        sentence = re.sub(r'\b' + re.escape(word) + r'\b', '', sentence)
    words = re.split(r'\s+', string)
    # Remove any empty strings resulting from multiple spaces
    words = [word for word in words if word]
    raise NotImplementedError


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
