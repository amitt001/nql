import re, collections

def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(file('verybig.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   print('splits:', splits)
   deletes    = [a + b[1:] for a, b in splits if b]
   print('deletes',deletes)
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   print('trans',transposes)
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   print('replaces', replaces)
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   print('inserts', inserts)
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): 
    f = open('file.txt', 'a')
    return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)
