from Count_vectorizer import CountVectorizer
import numpy as np


class TfidfTransformer():
    """
    Transforms matrix with numbers into tf-idf matrix
    Has parameter to_round = True by default
    """
    def __init__(self, to_round=True):
        self.to_round = to_round

    def tf_transform(self, count_matrix):
        if self.to_round:
            return [[round(x/sum(row), 3) for x in row]
                    for row in count_matrix]
        else:
            return [[x / sum(row) for x in row]
                    for row in count_matrix]

    def idf_transform(self, count_matrix):
        n = len(count_matrix)
        idf_matrix = []
        for i in range(len(count_matrix[0])):
            count = 0
            for j in range(n):
                if count_matrix[j][i] > 0:
                    count += 1
            if self.to_round:
                idf_i = round(np.log((n + 1) / (count + 1)) + 1, 3)
            else:
                idf_i = np.log((n + 1) / (count + 1)) + 1
            idf_matrix.append(idf_i)
        return idf_matrix

    def fit_transform(self, count_matrix):
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        if self.to_round:
            return [[round(row[i] * idf[i], 3) for i in range(len(row))]
                    for row in tf]
        else:
            return [[row[i] * idf[i] for i in range(len(row))]
                    for row in tf]


class TfidfVectorizer(CountVectorizer, TfidfTransformer):
    """
    Transforms corpus of texts into tf-idf matrix
    Has parameter to_round = True by default
    """
    def __init__(self, lowercase=True, to_round=True):
        CountVectorizer.__init__(self, lowercase)
        TfidfTransformer.__init__(self, to_round)

    def get_feature_names(self):
        return super().get_feature_names()

    def fit_transform(self, texts):
        matrix = CountVectorizer.fit_transform(self, texts)
        final_matrix = TfidfTransformer.fit_transform(self, matrix)
        return final_matrix


if __name__ == '__main__':
    cmatrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    transformer = TfidfTransformer()
    print(transformer.fit_transform(cmatrix))

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = TfidfVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())
