__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/22/2020 7:55 PM'

from collections import Counter
import itertools

docs = [
    "it is a good day, I like to stay here",
    "I am happy to be here",
    "I am bob",
    "it is sunny today",
    "I have a party today",
    "it is a dog and that is a cat",
    "there are dog and cat on the tree",
    "I study hard this morning",
    "today is a good day",
    "tomorrow will be a good day",
    "I like coffee, I like book and I like apple",
    "I do not like it",
    "I am kitty, I like bob",
    "I do not care who like bob, but I like kitty",
    "It is coffee time, bring your cup",
]

docs_words = [d.replace(",", "").split(" ") for d in docs]
vocab = set(itertools.chain(*docs_words))
print(vocab)
v2i = {v: i for i, v in enumerate(vocab)}
i2v = {i: v for v, i in v2i.items()}