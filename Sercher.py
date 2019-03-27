# coding: utf-8

import pandas as pd
import random

blue_df = pd.read_csv('blue_sky_books.csv')


class All:
    @staticmethod
    def get_all():
        return blue_df.to_json(force_ascii=False)


class word_search:
    @staticmethod
    def Searcher(wont_serch: str, serch_word: str):
        title_df = blue_df[blue_df[wont_serch].str.contains(serch_word)]

        return title_df.to_json(force_ascii=False)

    @staticmethod
    def Random_searcher(want_object):
        ls = list(range(1, 16224))
        random_df = pd.DataFrame(blue_df.take([random.choice(ls)]))

        return random_df.to_json(force_ascii=False)
    @staticmethod
    def Random_Scraping():
        url = pd.read_json(word_search.Random_searcher())

        return url


class get_list:
    @staticmethod
    def get_list():
        pass
