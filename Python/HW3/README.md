Задание: Реализуйте класс CountVectorizer, имеющий метод fit_transform.

```
corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
_ 'fresh', 'ingredients', 'parmesan', 'to', 'taste']
print(count_matrix)
Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
 ```
