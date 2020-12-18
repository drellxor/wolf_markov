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
    def __init__(self, dataset_path, pictures_path):
        models = []
        for item in os.listdir(dataset_path):
            file = os.path.join(dataset_path, item)
            if not os.path.isfile(file):
                continue
            with open(file, 'r') as f:
                model = POSifiedText(f.read())
            models.append(model)
        self.__model = markovify.combine(models)

        pics = []
        for item in os.listdir(pictures_path):
            file = os.path.join(pictures_path, item)
            if not os.path.isfile(file):
                continue
            with open(file, 'r') as f:
                pics += f.readlines()
        self.__pics = pics

    def make_quote(self):
        quote = self.__model.make_sentence().replace(' ,', ',').replace(' .', '.')

        r = requests.get(random.choice(self.__pics))
        while not r.content:
            r = requests.get(random.choice(self.__pics))
        pic = BytesIO(r.content)
        return quote, pic
