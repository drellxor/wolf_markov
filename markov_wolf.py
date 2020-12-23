from builtins import enumerate

import markovify
import ru2
import os
import requests
import random
from io import BytesIO

nlp = ru2.load_ru2('ru2')


class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


class MarkovWolf:
    def __init__(self, dataset_paths, dataset_weights, pictures_paths):
        models = []
        weights = []
        for dataset_path, weight in zip(dataset_paths, dataset_weights):
            for item in os.listdir(dataset_path):
                file = os.path.join(dataset_path, item)
                if not os.path.isfile(file):
                    continue
                with open(file, 'r', encoding='utf8') as f:
                    model = POSifiedText(f.read(), state_size=3)
                models.append(model)
                weights.append(weight)
        self.__model = markovify.combine(models, weights=weights)

        pics = []
        for pictures_path in pictures_paths:
            for item in os.listdir(pictures_path):
                file = os.path.join(pictures_path, item)
                if not os.path.isfile(file):
                    continue
                with open(file, 'r', encoding='utf8') as f:
                    pics += f.readlines()
        self.__pics = pics

    def make_quote(self):
        quote = None
        while not quote:
            quote = self.__model.make_sentence()
        quote = quote.replace(' ,', ',').replace(' .', '.')

        r = requests.get(random.choice(self.__pics))
        while not r.content:
            r = requests.get(random.choice(self.__pics))
        pic = BytesIO(r.content)
        return quote, pic
