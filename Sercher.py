import pandas as pd
import random

blue_df = pd.read_csv('blue_sky_books.csv', encoding='utf-8')


class word_serch:
    def Sercher(self, wont_serch: str, serch_word: str):
        title_df = blue_df[blue_df[wont_serch].str.contains(serch_word)]

        return title_df.to_json(force_ascii=False)

class random_serch:
    def Sercher(self):
        ls = range(1, 16224)
        random_df = blue_df.take([random.choice(ls)])

        return random_df

