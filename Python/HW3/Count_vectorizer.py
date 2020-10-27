class CountVectorizer():
    """
    Class that has functions fit_transform and
    get_feature_names.
    Class has attributes lowercase and _vocabulary.
    """
    stop_words = ("the", "a", "and")

    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = {}

    def get_feature_names(self):
        return self._vocabulary

    def fit_transform(self, texts):
        """Сounts the number of occurrences of each word
        from the word corpus in a specific sentence."""

        if self.lowercase:
            texts = [sentence.lower() for sentence in texts]

        vocab_pre = []

        for x in texts:
            words = x.split()
            for w in words:
                if w in vocab_pre or w in CountVectorizer.stop_words:
                    continue
                else:
                    vocab_pre.append(w)

        self._vocabulary = {i: item for i, item in enumerate(vocab_pre)}

        final = []
        for sentence in texts:
            pre_final = []
            for q in self._vocabulary.values():
                pre_final.append(sentence.split().count(q))
            final.append(pre_final)

        return final


if __name__ == '__main__':
    corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
