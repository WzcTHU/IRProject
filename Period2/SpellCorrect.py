import re, collections, json, time

class SpellCorrect:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.NWORDS = {}

    def words(self, text): return re.findall('[a-z]+', text.lower()) 

    def train(self, features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model

    def TrainNWORDS(self, filename='big.txt'):
        NWORDS = self.train(self.words(open('big.txt').read()))
        f_w = open('NWORDS.txt', 'w')
        f_w.write(json.dumps(NWORDS))
        f_w.close()

    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    def LoadNWORDS(self, filename='NWORDS.txt'):
        with open(filename, 'r') as json_file:
            self.NWORDS = json.load(json_file)

    def edits1(self, word):
        n = len(word)
        return set([word[0:i]+word[i+1:] for i in range(n)] +                     # deletion
                [word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] + # transposition
                [word[0:i]+c+word[i+1:] for i in range(n) for c in self.alphabet] + # alteration
                [word[0:i]+c+word[i:] for i in range(n+1) for c in self.alphabet])  # insertion

    def known_edits2(self, word):
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)

    def known(self, words): return set(w for w in words if w in self.NWORDS)

    def correct(self, word):
        self.LoadNWORDS()
        candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word]
        return max(candidates, key=lambda w: self.NWORDS[w])

if __name__ == '__main__':
    # print(type(NWORDS))
    m_c = SpellCorrect()
    start_time = time.process_time()
    print(m_c.correct('happiness'))
    print(time.process_time() - start_time)